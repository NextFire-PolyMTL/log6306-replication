# log6306-replication

## docker-pi-hole

| Commit   | Artefact   | Refactoring Type         | Technical Debt | Commentaires         |
| -------- | ---------- | ------------------------ | -------------- | -------------------- |
| 681d79f  | Dockerfile | Add ENV variable         | Maintenability |                      |
| d40ee18  |            |                          |                | maj de tests         |
| 782fb27  |            |                          |                | maj de tests         |
| d25aefb  | Dockerfile | Extract Run Instructions | Image size     |                      |
| e87b2ff6 |            |                          |                | merge commit d25aefb |
| 93e7dad  | Dockerfile | ?                        | Image size     | rm des caches        |


## hydra

| Commit   | False positive | Artefact       | Refactoring Type         | Technical Debt    | Commentaires                           |
| -------- | -------------- | -------------- | ------------------------ | ----------------- | -------------------------------------- |
| 03a28c3  |                | docker-compose | ?                        | Understandability | Séparation en plusieurs docker-compose |
| 95a51de  | x              |                |                          |                   | Patch qui fait référence à un refactor |
| 5508f2a  |                | Dockerfile     | ?                        | Understandability | Déplace dockerfile dans un dossier     |

## mail server

| Commit   | False positive | Artefact   | Refactoring Type         | Technical Debt    | Commentaires                            |
| -------- | -------------- | ---------- | ------------------------ | ----------------- | --------------------------------------- |
| 6faf5ce  |                | Dockerfile | Inline RUN instruciton   | Image size        |                                         |
| 2b4b829  | x              |            |                          |                   | Merge du commit precendant (6faf5ce)    |
| 9e1c478  | x              |            |                          |                   | Mise a jour de la documenation          |
| afe8cfb  | x              |            |                          |                   | Merge du commit precendant (9e1c478)    |
| afb8c05  |                | Dockerfile | Update Run insctruction  | Understandability |                                         |
| e4bab5b  | x              |            |                          |                   | Ajout de foncitonnalité (ELK)           |
| 021e942  | x              |            |                          |                   | Mise a jour de la documenation          |
| 66bc157  | x              |            |                          |                   |                                         |
| 08cd4d3  |                | Dockerfile | ?                        | Understandability | Ajout de commentaires                   |
| c851f5b  |                | Dockerfile | ?                        | Understandability | modification de commentaires            |
| b1a74bd  | x              |            |                          |                   |                                         |
| 7ca0568  | x              |            |                          |                   | Mise a jour de script et de fichier.pem |
| b9dbec3  | x              |            |                          |                   | Mise a jour de script                   |
| 22f68af  | x              |            |                          |                   | Merge d'une pull request                |
| 0bbec09  | x              |            |                          |                   | Mise a jour de scrip                    |
| 623d53b  | x              |            |                          |                   | Merge d'une pull request                |
| cb8e336  |                | Dockerfile |Inline RUN instruciton    | Image size        |                                         |
| 05db27f  | x              |            |                          |                   | Mise a jour de script                   |
| 88767f7  | x              |            |                          |                   | Déplacement de fichier                  |

## traefik

| Commit   | False positive | Artefact   | Refactoring Type         | Technical Debt    | Commentaires                            |
| -------- | -------------- | ---------- | ------------------------ | ----------------- | --------------------------------------- |
| 4d485e1  | x              |            |                          |                   | Refactore integration avec docker       |
| 2118f69  | x              |            |                          |                   | Pull request                            |
| d653a34  | x              |            |                          |                   |                                         |
| ae2ae85  | x              |            |                          |                   | Refactore integration avec docker       |
| 6e5f765  | x              |            |                          |                   | Refactor template                       |
| 50757b5  | x              |            |                          |                   | Refactor template                       |
| a533566  | x              |            |                          |                   | Refactore integration avec docker       |

## Grafana

| Commit   | False positive | Artefact   | Refactoring Type         | Technical Debt    | Commentaires                            |
| -------- | -------------- | ---------- | ------------------------ | ----------------- | --------------------------------------- |
| b4b3008  | x              |            |                          |                   | Pull request                            |
| 31b5db0  | x              |            |                          |                   | Pull request                            |
| 6310aaf  | x              |            |                          |                   | Definition du Dockerfile                |
| 008bee8  | x              |            |                          |                   | Pull request                            |
| cf1ebd5  | x              |            |                          |                   | Pull request                            |
| 1864807  | x              |            |                          |                   | Pull request                            |
| 5332871  | x              |            |                          |                   | Pull request                            |
| 3418224  | x              |            |                          |                   | Pull request                            |
| 1716b70  | x              |            |                          |                   | Pull request                            |
| d28d495  | x              |            |                          |                   | Pull request                            |
| f580c91  | x              |            |                          |                   | Definition du fichier docker-compose    |
| 845cebd  | x              |            |                          |                   | Mise a jour de documentation            |
| 616db7f  | x              |            |                          |                   | Pull request                            |