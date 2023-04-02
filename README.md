# log6306-replication

## hydra

| Commit  | False positive | Artefact       | Refactoring Type | Technical Debt    | Commentaires                           |
| ------- | -------------- | -------------- | ---------------- | ----------------- | -------------------------------------- |
| 03a28c3 |                | docker-compose | ?                | Understandability | Séparation en plusieurs docker-compose |
| 95a51de | x              |                |                  |                   | Patch qui fait référence à un refactor |
| 5508f2a |                | Dockerfile     | ?                | Understandability | Déplace dockerfile dans un dossier     |

## mail server

| Commit  | False positive | Artefact   | Refactoring Type        | Technical Debt    | Commentaires                            |
| ------- | -------------- | ---------- | ----------------------- | ----------------- | --------------------------------------- |
| 6faf5ce |                | Dockerfile | Inline RUN instruciton  | Image size        |                                         |
| 2b4b829 | x              |            |                         |                   | Merge du commit precendant (6faf5ce)    |
| 9e1c478 | x              |            |                         |                   | Mise a jour de la documenation          |
| afe8cfb | x              |            |                         |                   | Merge du commit precendant (9e1c478)    |
| afb8c05 |                | Dockerfile | Update Run insctruction | Understandability |                                         |
| e4bab5b | x              |            |                         |                   | Ajout de foncitonnalité (ELK)           |
| 021e942 | x              |            |                         |                   | Mise a jour de la documenation          |
| 66bc157 | x              |            |                         |                   |                                         |
| 08cd4d3 |                | Dockerfile | ?                       | Understandability | Ajout de commentaires                   |
| c851f5b |                | Dockerfile | ?                       | Understandability | modification de commentaires            |
| b1a74bd | x              |            |                         |                   |                                         |
| 7ca0568 | x              |            |                         |                   | Mise a jour de script et de fichier.pem |
| b9dbec3 | x              |            |                         |                   | Mise a jour de script                   |
| 22f68af | x              |            |                         |                   | Merge d'une pull request                |
| 0bbec09 | x              |            |                         |                   | Mise a jour de scrip                    |
| 623d53b | x              |            |                         |                   | Merge d'une pull request                |
| cb8e336 |                | Dockerfile | Inline RUN instruciton  | Image size        |                                         |
| 05db27f | x              |            |                         |                   | Mise a jour de script                   |
| 88767f7 | x              |            |                         |                   | Déplacement de fichier                  |

## traefik

| Commit  | False positive | Artefact | Refactoring Type | Technical Debt | Commentaires                      |
| ------- | -------------- | -------- | ---------------- | -------------- | --------------------------------- |
| 4d485e1 | x              |          |                  |                | Refactore integration avec docker |
| 2118f69 | x              |          |                  |                | Pull request                      |
| d653a34 | x              |          |                  |                |                                   |
| ae2ae85 | x              |          |                  |                | Refactore integration avec docker |
| 6e5f765 | x              |          |                  |                | Refactor template                 |
| 50757b5 | x              |          |                  |                | Refactor template                 |
| a533566 | x              |          |                  |                | Refactore integration avec docker |

## Grafana

| Commit  | False positive | Artefact                   | Refactoring Type                         | Technical Debt             | Commentaires                                                                    |
| ------- | -------------- | -------------------------- | ---------------------------------------- | -------------------------- | ------------------------------------------------------------------------------- |
| 0cc9cbc |                | docker-compose             | Reorder services                         | Understandability          | + ajout de `command:`                                                           |
| 01f1c1b | ?              |                            |                                          |                            | l'impr qu'ils ont fait que bouger plein de trucs                                |
| 4d18bda | x              |                            |                                          |                            | rajout d'un ADD (nouvelle fonc)                                                 |
| 5d5de23 | x              |                            |                                          |                            | nouvelle fonctionnalité                                                         |
| 5d72067 |                | Dockerfile, docker-compose | Update RUN instruction, Update image TAG | ?                          |                                                                                 |
| 6a8643b |                | Dockerfile                 | Update base image tag                    | ?                          |                                                                                 |
| 6be416d |                | docker-compose             | Rename service                           |                            |                                                                                 |
| 6ff1144 |                | docker-compose             | ?                                        | Maintenability, Build time | Utilisation d'une image existante pour le même service, suppression d'un volume |
| 7b68e6e |                | Dockerfile                 | ?                                        | Image size                 | Moins de COPY                                                                   |
| 07d78da | x              |                            |                                          |                            | Nouvelle image droneci                                                          |
| 9a61d43 | x              |                            |                                          |                            | Dockerfile initial                                                              |
| 9af809f |                | docker-compose             | Rename service                           | Understandability          | + ajout `ports:`                                                                |
| 9c086be |                | Dockerfile                 | Update base image tag                    | ?                          |                                                                                 |
| 9f4d4a9 |                | Dockerfile                 | ?                                        | ?                          | update ENV                                                                      |
| 25bcdbc | ?              | Dockerfile                 |                                          |                            | rajout d'un item à `apt install`                                                |
| 31b5db0 |                | Docekrfile                 | ?                                        | ?                          | Remplacement de ENV PATH par des `ln -s` dans `/usr/bin/`                       |
| 37bb5ef | ?              | Docekrfile                 |                                          |                            | rajout d'un item à `pip install`                                                |
| 44cef75 |                | docker-compose             | ?                                        | ?                          | suppression networks + rajout volumes                                           |
| 52fe6b0 | x              |                            |                                          |                            | nouvelle fonctionnalité                                                         |
| 63e7330 |                | Dockerfile                 | Update base image tag                    | ?                          |                                                                                 |
| 72d5215 | x              |                            |                                          |                            | doublon 63e7330                                                                 |
| 87db2d1 |                | Dockerfile                 | ?                                        |                            | update ENV                                                                      |
| 578a8e8 | x              |                            |                                          |                            |                                                                                 |
| 615de9b |                | docker-compose             | Rename service                           | Understandability          |                                                                                 |
| 627a32e |                | Dockerfile                 | Update base image tag                    | ?                          |                                                                                 |
| 940f510 | x              |                            |                                          |                            |                                                                                 |
| 5153d8e | x              |                            |                                          |                            | doublon 87db2d1                                                                 |
| 5739ad3 |                | Dockerfile                 | Update base image tag                    | Maintenability             | FROM arg                                                                        |
| 6310aaf | x              |                            |                                          |                            |                                                                                 |
| 8379a53 |                | Dockerfile                 | Add ARG instruction                      | Maintenability             |                                                                                 |
| 23738ad | x              |                            |                                          |                            |                                                                                 |
| 56927e5 | ?              | Dockerfile                 |                                          |                            | rajout d'un COPY                                                                |
| 79986e5 | x              |                            |                                          |                            | nouvelle fonc                                                                   |
| 594051b | x              |                            |                                          |                            |                                                                                 |
| a0e1a1a | x              |                            |                                          |                            | tests                                                                           |
| a1b9236 |                | docker-compose             | ?                                        | ?                          | update ENV                                                                      |
| abd5a74 | x              |                            |                                          |                            | doublon de 01f1c1b                                                              |
| b4b3008 | x              |                            |                                          |                            | doublon                                                                         |
| ba9d511 | x              |                            |                                          |                            | doublon                                                                         |
| c19a47d | x              |                            |                                          |                            | doublon                                                                         |
| c71904e | x              |                            |                                          |                            | doublon de 0cc9cbc                                                              |
| cc427b1 |                | Dockerfile                 | Update base image tag                    | Maintenability             | mais aussi fixed -> latest                                                      |
| d0f8d03 | x              |                            |                                          |                            | doublon                                                                         |
| d28d495 | ?              | Dockerfile                 | ?                                        | ?                          | nouvelle dépendance                                                             |
| d87bf30 |                | docker-compose             | Rename container                         | Maintenability             |                                                                                 |
| e58f3a6 | x              |                            |                                          |                            | doublon 44cef75                                                                 |
| f580c91 | x              |                            |                                          |                            | nouvelle fonc                                                                   |
| f717082 |                | docker-compose             | ?                                        | ?                          | remplacement network par lien entre 2 containers (2018 hein)                    |

## prometheus

| Commit  | False positive | Artefact   | Refactoring Type                                                                                            | Technical Debt | Commentaires        |
| ------- | -------------- | ---------- | ----------------------------------------------------------------------------------------------------------- | -------------- | ------------------- |
| 2bb3efc |                | Dockerfile | Replace ADD with COPY, Inline Run Instructions, Update base image, Update Run Instruction, Add ENV variable | Image size     |                     |
| af99960 | x              |            |                                                                                                             |                | inclus dans 2bb3efc |
| c453445 |                | Dockerfile | Extract stage                                                                                               |                | ajout de base       |

## rclone

None

## docker-pi-hole

| Commit  | False positive | Artefact   | Refactoring Type         | Technical Debt            | Commentaires                   |
| ------- | -------------- | ---------- | ------------------------ | ------------------------- | ------------------------------ |
| 71d77b5 |                | Dockerfile | Add ENV variable         | Maintenability            |                                |
| 93e7dad |                | Dockerfile | ?                        | Image size                | rm des caches                  |
| 611df9b | ?              | Dockerfile |                          |                           | rename d'un ENV                |
| 970c45c |                | Dockerfile | Update Base Image        | Maintenability/Image size | debian slim                    |
| 1970ffd |                | Dockerfile | ?                        | Maintenability            | rename Dockerfile.sh -> cmd.sh |
| 318720f | ?              | Dockerfile |                          |                           | maj dependances                |
| e7e9004 | x              |            |                          |                           |                                |
| e87b2ff |                | Dockerfile | Extract Run Instructions | Image size                |                                |
