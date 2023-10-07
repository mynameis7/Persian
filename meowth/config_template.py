'''Configuration values for Meowth - Rename to config.py'''

# bot token from discord developers
bot_token = 'your_token_here'

# default bot settings
bot_prefix = '!'
bot_master = 12345678903216549878
bot_coowners = [132314336914833409, 263607303096369152]
preload_extensions = []
version = '3'

# minimum required permissions for bot user
bot_permissions = 268822736

# postgresql database credentials
db_details = {
    # 'username' : 'meowth',
    # 'database' : 'meowth',
    # 'hostname' : 'localhost',
    'password' : 'password'
}

dbdocid = 'google_sheet_id_here'

emoji = {
    'maybe': '🙋',
    'coming': '🚗',
    'here': '<:here:1160071226488803359>',
    'remote': '🛰',
    'invite': '✉',
    'cancel': '❌'
}

# default language
lang_bot = 'en'
lang_pkmn = 'en'

# team settings
team_list = ['mystic', 'valor', 'instinct']
team_colours = {
    "mystic"   : "0x3498db",
    "valor"    : "0xe74c3c",
    "instinct" : "0xf1c40f"
}

team_emoji = {
    "mystic"   : "<:mystic:1159751462851719248>",
    "valor"    : "<:valor:1159751395260497980>",
    "instinct" : "<:instinct:1159752582852530176>",
    "unknown" : "\u2754"
}

# raid settings
allow_assume = {
    "5" : "False",
    "4" : "False",
    "3" : "False",
    "2" : "False",
    "1" : "False"
}

status_emoji = {
    "omw"     : ":omw:",
    "here" : ":here:"
}

type_emoji = {
    "bug"      : { "typeid" : "POKEMON_TYPE_BUG",      "emoji" : "<:bug:1159751555491311696>",     "weather" : "RAINY" },
    "dark"     : { "typeid" : "POKEMON_TYPE_DARK",     "emoji" : "<:dark:1159751556254683137>",     "weather" : "FOG" },
    "dragon"   : { "typeid" : "POKEMON_TYPE_DRAGON",   "emoji" : "<:dragon:1159751558578323477>",   "weather" : "WINDY" },
    "electric" : { "typeid" : "POKEMON_TYPE_ELECTRIC", "emoji" : "<:electric:1159751563158507540>", "weather" : "RAINY" },
    "fairy"    : { "typeid" : "POKEMON_TYPE_FAIRY",    "emoji" : "<:fairy:1159751557701705800>",    "weather" : "OVERCAST" },
    "fighting" : { "typeid" : "POKEMON_TYPE_FIGHTING", "emoji" : "<:fighting:1159751521739735090>", "weather" : "OVERCAST" },
    "fire"     : { "typeid" : "POKEMON_TYPE_FIRE",     "emoji" : "<:fire:1159753585203085332>",    "weather" : "CLEAR" },
    "flying"   : { "typeid" : "POKEMON_TYPE_FLYING",   "emoji" : "<:flying:1159751559270379541>",   "weather" : "WINDY" },
    "ghost"    : { "typeid" : "POKEMON_TYPE_GHOST",    "emoji" : "<:ghost:1159751520942837760>",   "weather" : "FOG" },
    "grass"    : { "typeid" : "POKEMON_TYPE_GRASS",    "emoji" : "<:grass:1159751522834452553>",    "weather" : "CLEAR" },
    "ground"   : { "typeid" : "POKEMON_TYPE_GROUND",   "emoji" : "<:ground:1159752578578526208>",   "weather" : "CLEAR" },
    "ice "     : { "typeid" : "POKEMON_TYPE_ICE",      "emoji" : "<:ice:1159751525191647272>",      "weather" : "SNOW" },
    "normal"   : { "typeid" : "POKEMON_TYPE_NORMAL",   "emoji" : "<:normal:1159752581766189056>",   "weather" : "PARTLY_CLOUDY" },
    "poison"   : { "typeid" : "POKEMON_TYPE_POISON",   "emoji" : "<:poison:1159752579992014890>",   "weather" : "OVERCAST" },
    "psychic"  : { "typeid" : "POKEMON_TYPE_PSYCHIC",  "emoji" : "<:psychic:1159751562047008810>",  "weather" : "WINDY" },
    "rock"     : { "typeid" : "POKEMON_TYPE_ROCK",     "emoji" : "<:rock:1159751523522326578>",     "weather" : "PARTLY_CLOUDY" },
    "steel"    : { "typeid" : "POKEMON_TYPE_STEEL",    "emoji" : "<:steel:1159751525925662810>",    "weather" : "SNOW" },
    "water "   : { "typeid" : "POKEMON_TYPE_WATER",    "emoji" : "<:water:1159751524235345980>",    "weather" : "RAINY" }
}


raid_times = {
    1: (60, 45),
    2: (60, 45),
    3: (60, 45),
    4: (60, 45),
    5: (60, 45),
    "EX": (None, 45)
}

# weatherapikey = 

max_report_distance = 20

# help command categories
command_categories = {
    "Owner" : {
        "index"       : "5",
        "description" : "Owner-only commands for bot config or info."
    },
    "Server Config" : {
        "index"       : "10",
        "description" : "Server configuration commands."
    },
    "Bot Info" : {
        "index"       : "15",
        "description" : "Commands for finding out information on the bot."
    },
}

# analytics/statistics
pokebattler_tracker = "MeowthSelfHoster"
