descriptions = [
    ("Difficulty", "Alters the overall challenge level of the game."),
    (
        "DayTimeSpeedRate",
        "Modifies the speed of in-game time during daytime.",
    ),
    ("NightTimeSpeedRate", "Modifies the speed of in-game time during nighttime."),
    ("ExpRate", "Alters the rate at which both players and creatures gain experience."),
    (
        "PalCaptureRate",
        "Adjusts the likelihood of successfully capturing Pals.",
    ),
    (
        "PalSpawnNumRate",
        "Controls the frequency at which Pals appear in the game world.",
    ),
    ("PalDamageRateAttack", "Fine tunes the damage dealt by Pals in combat."),
    (
        "PalDamageRateDefense",
        "Fine tunes the damage received by Pals in combat.",
    ),
    ("PlayerDamageRateAttack", "Fine tunes the damage dealt by players in combat."),
    ("PlayerDamageRateDefense", "Fine tunes the damage received by players in combat."),
    (
        "PlayerStomachDecreaceRate",
        "Adjusts the rate at which the player’s stomach depletes.",
    ),
    (
        "PlayerStaminaDecreaceRate",
        "Adjusts the rate at which the player’s stamina depletes.",
    ),
    (
        "PlayerAutoHPRegeneRate",
        "Modifies the rate of automatic health regeneration for players.",
    ),
    (
        "PlayerAutoHpRegeneRateInSleep",
        "Modifies the rate of automatic health regeneration for players during sleep.",
    ),
    (
        "PalStomachDecreaceRate",
        "Adjusts the rate at which Pals get hungry.",
    ),
    (
        "PalStaminaDecreaceRate",
        "Adjusts the rate at which Pals stamina depletes.",
    ),
    (
        "PalAutoHPRegeneRate",
        "Modifies the rate of automatic health regeneration for Pals.",
    ),
    (
        "PalAutoHpRegeneRateInSleep",
        "Modifies the rate of automatic health regeneration for Pals during sleep.",
    ),
    (
        "BuildObjectDamageRate",
        "Adjusts the rate at which constructed objects sustain damage.",
    ),
    (
        "BuildObjectDeteriorationDamageRate",
        "Controls the rate at which built objects deteriorate over time.",
    ),
    (
        "CollectionDropRate",
        "Adjusts the likelihood of obtaining items when collecting resources.",
    ),
    ("CollectionObjectHpRate", "Adjusts the health of objects collected in the game."),
    (
        "CollectionObjectRespawnSpeedRate",
        "Adjusts the speed at which collected objects respawn in the game world.",
    ),
    (
        "EnemyDropItemRate",
        "Modifies the likelihood of enemies dropping items upon defeat.",
    ),
    (
        "DeathPenalty",
        "Specifies the penalty incurred by players upon death. Available options are None = Nothing dropped, Item = Drops only items in your inventory, ItemAndEquipment = Drops Items in your inventory and your equipment, All = Drops everything including equipped Pals",
    ),
    (
        "bEnablePlayerToPlayerDamage",
        "Enables or disables the ability for players to inflict damage on each other.",
    ),
    (
        "bEnableFriendlyFire",
        "Enables or disables the occurrence of friendly fire among players.",
    ),
    (
        "bEnableInvaderEnemy",
        "Enables or disables the presence of invader enemies in the game.",
    ),
    (
        "bActiveUNKO",
        "Activates or deactivates UNKO (Unidentified Nocturnal Knock-off) in the game.",
    ),
    (
        "bEnableAimAssistPad",
        "Enables or disables aim assist for players using controllers.",
    ),
    (
        "bEnableAimAssistKeyboard",
        "Enables or disables aim assist for players using keyboards.",
    ),
    (
        "DropItemMaxNum",
        "Sets the maximum number of dropped items that can exist in the game.",
    ),
    (
        "DropItemMaxNum_UNKO",
        "Sets the maximum number of dropped UNKO items that can exist in the game.",
    ),
    (
        "BaseCampMaxNum",
        "Sets the maximum number of base camps that players can construct. This setting is global across the server, it is not specific to individual guilds.",
    ),
    (
        "BaseCampWorkerMaxNum",
        "Sets the maximum number of workers that can be assigned to a base camp.",
    ),
    (
        "DropItemAliveMaxHours",
        "Sets the maximum duration for which dropped items remain in the game world.",
    ),
    (
        "bAutoResetGuildNoOnlinePlayers",
        "Automatically resets guilds with no online players.",
    ),
    (
        "AutoResetGuildTimeNoOnlinePlayers",
        "Sets the time after which guilds with no online players are automatically reset.",
    ),
    (
        "GuildPlayerMaxNum",
        "Sets the maximum number of players that can belong to a guild.",
    ),
    ("PalEggDefaultHatchingTime", "Sets the default hatching time for Pal eggs."),
    ("WorkSpeedRate", "Adjusts the overall work speed within the game."),
    ("bIsMultiplay", "Enables or disables the multiplayer mode."),
    ("bIsPvP", "Enables or disables player versus player (PvP) mode."),
    (
        "bCanPickupOtherGuildDeathPenaltyDrop",
        "Enables or disables the pickup of death penalty drops from other guilds.",
    ),
    (
        "bEnableNonLoginPenalty",
        "Enables or disables penalties for players who are not logged in.",
    ),
    ("bEnableFastTravel", "Enables or disables the fast travel feature."),
    (
        "bIsStartLocationSelectByMap",
        "Enables or disables the selection of starting locations on the in-game map.",
    ),
    (
        "bExistPlayerAfterLogout",
        "Enables or disables the persistence of players in the game world after logout.",
    ),
    (
        "bEnableDefenseOtherGuildPlayer",
        "Enables or disables the defense of other guild players.",
    ),
    (
        "CoopPlayerMaxNum",
        "Sets the maximum number of cooperative players allowed in a session. This setting does not appear to have any effect in dedicated servers and is safe to leave at its default.",
    ),
    (
        "ServerPlayerMaxNum",
        "Sets the maximum number of players allowed on the server. Make sure your server machine has enough ram. Expect to have about 1.5GB of RAM usage per connected player.",
    ),
    ("ServerName", "Sets the name of the Palworld server."),
    ("ServerDescription", "Provides a description for the Palworld server."),
    ("AdminPassword", "Sets the password for server administration."),
    (
        "ServerPassword",
        "Sets the password for joining the Palworld server. Leave this setting blank due to a bug as of Palworld version 0.1.2.0.",
    ),
    (
        "PublicPort",
        "Sets the public port for the Palworld server. This setting is required to have your server shown in the Community Servers tab.",
    ),
    (
        "PublicIP",
        "Sets the public IP address for the Palworld server. This setting is required to have your server shown in the Community Servers tab.",
    ),
    (
        "RCONEnabled",
        "Enables or disables Remote Console (RCON) for server administration.",
    ),
    ("RCONPort", "Sets the port for Remote Console (RCON) communication."),
    (
        "Region",
        "Sets the region for the Palworld server. Options appear to be NA, SA, China, Asia, EU, JP.",
    ),
    ("bUseAuth", "Enables or disables server authentication."),
    (
        "BanListURL",
        "Sets the URL for the server’s ban list. The default is the Global BanList",
    ),
]
