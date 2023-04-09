# log6306-replication

## hydra

| Commit  | False positive   | Artefact       | Refactoring Type      | Technical Debt    | Commentaires                           |
| ------- | ---------------- | -------------- | --------------------- | ----------------- | -------------------------------------- |
| 03a28c3 |                  | docker-compose | Move services         | Understandability | Séparation en plusieurs docker-compose |
| 56bce67 | (pas un refacto) | Dockerfile     |                       |                   | maj de la commande de build            |
| 95a51de | x                |                |                       |                   | Patch qui fait référence à un refactor |
| 5508f2a |                  | Dockerfile     | **Move Docker files** | Understandability | Déplace dockerfile dans un dossier     |
| 062734e | (pas un refacto) | docker-compose |                       |                   | maj de la command d'un service         |

## mail server

| Commit  | False positive   | Artefact   | Refactoring Type            | Technical Debt    | Commentaires                           |
| ------- | ---------------- | ---------- | --------------------------- | ----------------- | -------------------------------------- |
| 2b4b829 | x                |            |                             |                   | Merge du commit precendant (6faf5ce)   |
| 6faf5ce |                  | Dockerfile | Inline RUN instruciton      | Image size        |                                        |
| 08cd4d3 | (pas un refacto) | Dockerfile |                             |                   | Ajout de commentaires                  |
| 9e1c478 | x                |            |                             |                   | Mise a jour de la documenation         |
| 5254f7c | (pas un refacto) | Dockerfile |                             |                   | Ajout d'un COPY                        |
| ae6f41e |                  | Dockerfile | Update Run insctruction     | Understandability |                                        |
| afb8c05 |                  | Dockerfile | Update Run insctruction     | Understandability |                                        |
| afe8cfb | x                |            |                             |                   | Merge du commit precendant (9e1c478)   |
| b61dfe1 | (pas un refacto) | Dockerfile |                             |                   | scripts supplémentaires dans COPY      |
| c851f5b | (pas un refacto) | Dockerfile |                             |                   | modification de commentaires           |
| c881fac |                  | Dockerfile | Update Run insctruction     | Understandability |                                        |
| cb8e336 |                  | Dockerfile | Inline RUN instruciton      | Image size        |                                        |
| da81713 |                  | Dockerfile | **Update COPY instruction** | Understandability | Update ordre des fichiers dans un COPY |
| e4bab5b | x                |            |                             |                   | Ajout de foncitonnalité (ELK)          |

## traefik

| Commit  | False positive   | Artefact   | Refactoring Type                                  | Technical Debt                    | Commentaires                      |
| ------- | ---------------- | ---------- | ------------------------------------------------- | --------------------------------- | --------------------------------- |
| 1bccbf0 | (pas un refacto) | Dockerfile |                                                   |                                   | maj flags d'une commande d'un RUN |
| 257dbd1 | x                |            |                                                   |                                   |                                   |
| f54fa10 |                  | Dockerfile | Replace ADD with COPY, **Replace ENTRYPOINT/CMD** | Maintenability, Understandability | + remplacement CMD par ENTRYPOINT |

## Grafana

| Commit  | False positive   | Artefact                   | Refactoring Type                                | Technical Debt             | Commentaires                                                                    |
| ------- | ---------------- | -------------------------- | ----------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------- |
| 0cc9cbc |                  | docker-compose             | Reorder services                                | Understandability          | ajout de `command:`                                                             |
| 01f1c1b | x                |                            |                                                 |                            | l'impr qu'ils ont fait que bouger plein de trucs                                |
| 4d18bda | x                |                            |                                                 |                            | rajout d'un ADD (nouvelle fonc)                                                 |
| 5d5de23 | x                |                            |                                                 |                            | nouvelle fonctionnalité                                                         |
| 5d72067 |                  | Dockerfile, docker-compose | Update RUN instruction, Update image TAG        | Maintenability             |                                                                                 |
| 6a8643b | (pas un refacto) | Dockerfile                 |                                                 |                            | FROM maj mineure                                                                |
| 6be416d |                  | docker-compose             | Rename service                                  |                            |                                                                                 |
| 6ff1144 |                  | docker-compose             | Update base image                               | Maintenability, Build time | Utilisation d'une image existante pour le même service, suppression d'un volume |
| 7b68e6e | (pas un refacto) | Dockerfile                 |                                                 | Image size                 | Moins de COPY                                                                   |
| 07d78da | x                |                            |                                                 |                            | Nouvelle image droneci                                                          |
| 9a61d43 | x                |                            |                                                 |                            | Dockerfile initial                                                              |
| 9af809f |                  | docker-compose             | Rename service, Extract Ports Attribute         | Understandability          | ajout `ports:`                                                                  |
| 9c086be | (pas un refacto) | Dockerfile                 |                                                 |                            | FROM maj mineure                                                                |
| 9f4d4a9 | (pas un refacto) | Dockerfile                 |                                                 |                            | update ENV                                                                      |
| 25bcdbc | (pas un refacto) | Dockerfile                 |                                                 |                            | rajout d'un item à `apt install`                                                |
| 31b5db0 | (pas un refacto) | Docekrfile                 |                                                 |                            | Remplacement de ENV PATH par des `ln -s` dans `/usr/bin/`                       |
| 37bb5ef | (pas un refacto) | Docekrfile                 |                                                 |                            | rajout d'un item à `pip install`                                                |
| 44cef75 |                  | docker-compose             | **Update networking**, Extract Volume Attribute | Maintenability             | suppression networks + rajout volumes                                           |
| 52fe6b0 | x                |                            |                                                 |                            | nouvelle fonctionnalité                                                         |
| 63e7330 | (pas un refacto) | Dockerfile                 |                                                 |                            | FROM maj mineure                                                                |
| 72d5215 | x                |                            |                                                 |                            | doublon 63e7330                                                                 |
| 87db2d1 | (pas un refacto) | Dockerfile                 |                                                 |                            | update ENV                                                                      |
| 578a8e8 | x                |                            |                                                 |                            |                                                                                 |
| 615de9b |                  | docker-compose             | Rename service                                  | Understandability          |                                                                                 |
| 627a32e | (pas un refacto) | Dockerfile                 |                                                 |                            | FROM maj mineure                                                                |
| 940f510 | x                |                            |                                                 |                            |                                                                                 |
| 5153d8e | x                |                            |                                                 |                            | doublon 87db2d1                                                                 |
| 5739ad3 |                  | Dockerfile                 | Update base image tag, Add ARG instruction      | Maintenability             | FROM arg                                                                        |
| 6310aaf | x                |                            |                                                 |                            |                                                                                 |
| 8379a53 |                  | Dockerfile                 | Add ARG instruction                             | Maintenability             |                                                                                 |
| 23738ad | x                |                            |                                                 |                            |                                                                                 |
| 56927e5 | (pas un refacto) | Dockerfile                 |                                                 |                            | rajout d'un COPY                                                                |
| 79986e5 | x                |                            |                                                 |                            | nouvelle fonc                                                                   |
| 594051b | x                |                            |                                                 |                            |                                                                                 |
| a0e1a1a | x                |                            |                                                 |                            | tests                                                                           |
| a1b9236 | (pas un refacto) | docker-compose             |                                                 |                            | update ENV                                                                      |
| abd5a74 | x                |                            |                                                 |                            | doublon de 01f1c1b                                                              |
| b4b3008 | x                |                            |                                                 |                            | doublon                                                                         |
| ba9d511 | x                |                            |                                                 |                            | doublon                                                                         |
| c19a47d | x                |                            |                                                 |                            | doublon                                                                         |
| c71904e | x                |                            |                                                 |                            | doublon de 0cc9cbc                                                              |
| cc427b1 |                  | Dockerfile                 | **Update base image tag**                       | Maintenability             | mais aussi fixed -> latest                                                      |
| d0f8d03 | x                |                            |                                                 |                            | doublon                                                                         |
| d28d495 | (pas un refacto) | Dockerfile                 |                                                 |                            | nouvelle dépendance                                                             |
| d87bf30 |                  | docker-compose             | Rename container                                | Maintenability             |                                                                                 |
| e58f3a6 | x                |                            |                                                 |                            | doublon 44cef75                                                                 |
| f580c91 | x                |                            |                                                 |                            | nouvelle fonc                                                                   |
| f717082 |                  | docker-compose             | **Update networking**                           | Maintenability             | remplacement network par lien entre 2 containers                                |

## prometheus

| Commit  | False positive | Artefact   | Refactoring Type                                                                                            | Technical Debt | Commentaires        |
| ------- | -------------- | ---------- | ----------------------------------------------------------------------------------------------------------- | -------------- | ------------------- |
| 2bb3efc |                | Dockerfile | Replace ADD with COPY, Inline Run Instructions, Update base image, Update Run Instruction, Add ENV variable | Image size     |                     |
| af99960 | x              |            |                                                                                                             |                | inclus dans 2bb3efc |
| c453445 |                | Dockerfile | Extract stage                                                                                               |                | ajout de base       |

## rclone

None

## docker-pi-hole

| Commit  | False positive   | Artefact   | Refactoring Type         | Technical Debt            | Commentaires                   |
| ------- | ---------------- | ---------- | ------------------------ | ------------------------- | ------------------------------ |
| 71d77b5 |                  | Dockerfile | Add ENV variable         | Maintenability            |                                |
| 93e7dad | (pas un refacto) | Dockerfile |                          |                           | rm des caches                  |
| 611df9b | (pas un refacto) | Dockerfile |                          |                           | rename d'un ENV                |
| 970c45c |                  | Dockerfile | Update Base Image        | Maintenability/Image size | debian slim                    |
| 1970ffd |                  | Dockerfile | **Rename script**        | Maintenability            | rename Dockerfile.sh -> cmd.sh |
| 318720f | (pas un refacto) | Dockerfile |                          |                           | maj dependances                |
| e7e9004 | x                |            |                          |                           |                                |
| e87b2ff |                  | Dockerfile | Extract Run Instructions | Image size                |                                |
