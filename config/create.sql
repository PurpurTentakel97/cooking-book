/*
Purpur Tentakel
Cocking Book
12.04.2023
*/

/* Raw Types */
CREATE TABLE IF NOT EXISTS "main"."raw_types"(
"ID" INTEGER NOT NULL UNIQUE,
"_created" INTEGER DEFAULT (CAST(strftime('%s', 'now') AS INTEGER)),
"_updated" INTEGER DEFAULT (CAST(strftime('%s', 'now') AS INTEGER)),
"type" TEXT NOT NULL UNIQUE,
PRIMARY KEY ("ID" AUTOINCREMENT)
);
/* Trigger */
CREATE TRIGGER IF NOT EXISTS "trigger_update_raw_types"
    AFTER UPDATE ON "raw_types"
BEGIN
    UPDATE "raw_types" SET _updated = CAST(strftime('%s', 'now') AS INTEGER) WHERE ID=OLD.id;
END;

/* Recipe */
CREATE TABLE IF NOT EXISTS "main"."recipes"(
"ID" INTEGER NOT NULL UNIQUE,
"_created" INTEGER DEFAULT (CAST(strftime('%s', 'now') AS INTEGER)),
"_updated" INTEGER DEFAULT (CAST(strftime('%s', 'now') AS INTEGER)),
"title" TEXT NOT NULL UNIQUE,
"description" TEXT NOT NULL,
PRIMARY KEY ("ID" AUTOINCREMENT)
);
/* Trigger */
CREATE TRIGGER IF NOT EXISTS "trigger_update_recipes"
    AFTER UPDATE ON "recipes"
BEGIN
    UPDATE "recipes" SET _updated = CAST(strftime('%s', 'now') AS INTEGER) WHERE ID=OLD.id;
END;

/* Ingredients */
CREATE TABLE IF NOT EXISTS "main"."ingredients"(
"ID" INTEGER NOT NULL UNIQUE,
"_created" INTEGER DEFAULT (CAST(strftime('%s', 'now') AS INTEGER)),
"_updated" INTEGER DEFAULT (CAST(strftime('%s', 'now') AS INTEGER)),
"recipe_id" INTEGER NOT NULL,
"amount" INTEGER NOT NULL,
"unit" TEXT,
"ingredient" TEXT NOT NULL,
PRIMARY KEY ("ID" AUTOINCREMENT),
FOREIGN KEY ("recipe_id") REFERENCES "recipes"
);
/* Trigger */
CREATE TRIGGER IF NOT EXISTS "trigger_update_ingredients"
    AFTER UPDATE ON "ingredients"
BEGIN
    UPDATE "ingredients" SET _updated = CAST(strftime('%s', 'now') AS INTEGER) WHERE ID=OLD.id;
END;

/* Types */
CREATE TABLE IF NOT EXISTS "main"."types"(
"ID" INTEGER NOT NULL UNIQUE,
"_created" INTEGER DEFAULT (CAST(strftime('%s', 'now') AS INTEGER)),
"_updated" INTEGER DEFAULT (CAST(strftime('%s', 'now') AS INTEGER)),
"recipe_id" INTEGER NOT NULL,
"raw_type_id" INTEGER NOT NULL,
PRIMARY KEY ("ID" AUTOINCREMENT),
FOREIGN KEY ("recipe_id") REFERENCES "recipes",
FOREIGN KEY ("raw_type_id") REFERENCES "raw_types"
);
/* Trigger */
CREATE TRIGGER IF NOT EXISTS "trigger_update_types"
    AFTER UPDATE ON "types"
BEGIN
    UPDATE "types" SET _updated = CAST(strftime('%s', 'now') AS INTEGER) WHERE ID=OLD.id;
END;