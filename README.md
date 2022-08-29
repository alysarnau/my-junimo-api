# my-junimo-api

# Summary: 
Finally, an app that makes resource and crafting management easy in Stardew Valley! This app allows you to manage the inventory of your character(s) and easily see if your inventory meets the requirements for crafting items (and larger projects!) inside Stardew Valley.

# Technologies Used
Django/SQL Backend (Python)
React Frontend

# Link to Client Side
https://github.com/alysvolatile/my-Junimo-Client

# Front End Deployed:
https://github.com/nickesparza/my-Junimo-Client

# Back End Deployed: 
https://my-junimo-api.herokuapp.com/

# Team:
Nick Esparza, Alys Cooper

# External API/Seed Data Used
* Twitter API (<a href='https://developer.twitter.com/en/products/twitter-api'>here</a>) to link to recent tweets from Stardew Valley developer ConcernedApe.
* Seed Data taken from the <a href='https://stardewvalleywiki.com/'>Stardew Valley Wiki</a>.

# ERDs
<img src='./my-junimo-helper-erd.png' max-width='800px'/>

# Whiteboarding of SQL relationships
<img src='./Images/SQL_relationship_diagram.jpg' max-width='800px'/>

# MVP MODELS (listed in ERD as well)
* User (for player) - name
* Characters Table - (one to many from user to characters; 'saves') (fully crudable) 
    - Name (string)
    - Platform (string)
    - Farm Type (string)
    - Pet Type (string)
    - Pet Name (string)
    - Pet image (if cat, choose cat images; if dog, choose dog images - are there pigs too?) (string)
    - Love Interest/Spouse (string)
    - Horse Name (string)
    - Total G
    - Year 
* Materials Table
    - material name
    - description
    - image
    - sale price
    - link to wiki page
* Inventory Table
    - ref Character id
    - ref Material id
    - Amount 
* Crafting Recipes Table
    - name
    - description
    - processor needed (eg. forge, kiln)
* Blueprint Materials Table
    - ref Crafting Recipe id
    - ref Material id
    - Amount needed


* STRETCH GOAL - Construction projects from Robin 
    - name
    - cost
    - required material array
    - previous requirements (big coop requires coop)

### USER route table

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| POST   | `/sign-in`             | `users#signin`    |
| PATCH  | `/change-password/`    | `users#changepw`  |
| DELETE | `/sign-out/`           | `users#signout`   |

### CHARACTER route table

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| GET    | `/view-all-characters` | `characters#view-all`   |
| GET    | `/view-character`        | `characters#view`   |
| POST   | `/create-character`      | `characters#create`    |
| PATCH  | `/edit-character/`       | `characters#edit`  |
| DELETE | `/delete-character/`     | `characters#delete`   |

### MATERIAL route table

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| GET    | `/view-material`        | `materials#view`   |
| GET    | `/view-all-materials`        | `materials#view-all`   |

### CRAFTING RECIPE route table

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| GET    | `/view-crafting-recipes`        | `crafting-recipes#view`   |
| GET    | `/view-all-crafting-recipes`        | `crafting-recipes#view-all`   |

### STRETCH GOAL - CONSTRUCTION BLUEPRINT route table

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| GET    | `/view-blueprint`        | `blueprints#view`   |
| GET    | `/view-all-blueprints`        | `blueprints#view-all`   |

# How to seed the database!

We have provided seed data for all materials and blueprints, as well as provided a seed TEMPLATE for inventory and recipe_materials. Please note the word TEMPLATE: since the recipe_material and template models both rely heavily on referencing other models existing in the database, some delicacy is required if you'd like to seed things with a csv. However, it is easy to do so with a little help! Here is that help.

## Seeding Materials
* In the terminal, run ```python manage.py runscript load_resources```. This will seed the database with materials.
* In the terminal, run ```python manage.py runscript load_blueprints```. This will seed the database with blueprints!
* <strong>PROVIDED THAT YOU HAVE ONLY RUN THE SEEDED FILES ONCE RESPECTIVELY AND ARE DEALING WITH A "CLEAN" DATABASE...</strong> (that is, a database where the IDs for materials and blueprints start at "1".)
* In the terminal, run ```python manage.py runscript blueprint_materials```. This will seed the database with the information that connects the materials and blueprints with their amount needed!