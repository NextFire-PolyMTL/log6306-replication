from pydriller import Repository
from queue import Queue
import threading
import json

class Info:
    def __init__(self, repo, commit, keywords):
        self.repo = repo
        self.commit = commit
        self.keywords = keywords
    
    def analyse(self, out_queue: Queue):
        msg = self.commit.msg.casefold()
        
        # check if any keyword are in the given commit
        found_keywords = True
        for k in self.keywords:
            found_keywords &= k in msg

        # send found back to handler
        if found_keywords:
            out_queue.put(self)

def analyse_commit(in_queue: Queue, out_queue: Queue):
    while (i := in_queue.get()) is not None:
        i.analyse(out_queue)

    # propagate close
    in_queue.put(None)


def main(n_thread: int, urls: list[str], keywords: list[str]):
    # casefold all input
    keywords = [k.casefold() for k in keywords]

    # create queue shared accross multiple threads
    in_queue = Queue()
    out_queue = Queue()

    # create worker threads
    workers = []
    for i in range (n_thread):
        th = threading.Thread(target=analyse_commit, args=(in_queue, out_queue))
        th.start()
        workers.append(th)

    # the actual working part
    results = {}
    for url in urls:
        results[url] = {"commits": []}
        for commit in Repository(url).traverse_commits():
            i = Info(url, commit, keywords)
            in_queue.put(i)
    
    # wait for thread completion
    in_queue.put(None)
    for th in workers:
        th.join()
    out_queue.put(None)
    
    # get output from all threads
    while (o := out_queue.get()) is not None:
        results[o.repo]["commits"].append(o.commit.hash)

    for r in results:
        results[r]["count"] = len(results[r]["commits"])
    
    # save results
    with open("commits.json", "w") as outfile:   
        json.dump(results, outfile, indent=4)
    print(results)

if __name__ == "__main__":
    repos = [
        "https://github.com/ory/hydra",
        "https://github.com/docker-mailserver/docker-mailserver",
        "https://github.com/traefik/traefik",
        "https://github.com/grafana/grafana",
        "https://github.com/prometheus/prometheus",
        "https://github.com/rclone/rclone",
        "https://github.com/pi-hole/docker-pi-hole",
    ]
    main(10, repos, ["docker", "refactor"])