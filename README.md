# log6306-replication

## prometheus

| Commit  | Artefact   | Refactoring Type                                                   | Technical Debt | Commentaires                |
| ------- | ---------- | ------------------------------------------------------------------ | -------------- | --------------------------- |
| af99960 | Dockerfile | Update base image, Inline Run Instructions, Update Run Instruction | Image size     |                             |
| 2bb3efc |            |                                                                    |                | merge commit af99960        |
| 93ecf0e |            |                                                                    |                | maj d'un module dockerswarm |

## rclone

| Commit  | Artefact | Refactoring Type | Technical Debt | Commentaires                  |
| ------- | -------- | ---------------- | -------------- | ----------------------------- |
| 221dfc3 |          |                  |                | refacto module `serve docker` |

## docker-pi-hole

| Commit   | Artefact   | Refactoring Type         | Technical Debt | Commentaires         |
| -------- | ---------- | ------------------------ | -------------- | -------------------- |
| 681d79f  | Dockerfile | Add ENV variable         | Maintenability |                      |
| d40ee18  |            |                          |                | maj de tests         |
| 782fb27  |            |                          |                | maj de tests         |
| d25aefb  | Dockerfile | Extract Run Instructions | Image size     |                      |
| e87b2ff6 |            |                          |                | merge commit d25aefb |
| 93e7dad  | Dockerfile | ?                        | Image size     | rm des caches        |
