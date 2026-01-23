Hooks.on('init', () => {
    foundry.utils.mergeObject(game.impmal.config.disciplines, {
        nurglitePowers: 'Nurglite Powers'
    });

    foundry.utils.mergeObject(game.impmal.config.npcRoles, {
        master: 'Master',
        overseer: 'Overseer '
    });

    foundry.utils.mergeObject(game.impmal.config.weaponArmourTraits, {
        accurate: 'Accurate',
        fast: 'Fast',
        sanctified: 'Sanctified',
        storm: 'Storm (X)',
        twinLinked: 'Twin-Linked',
        tripleLinked: 'Triple-Linked',
        vratine: 'Vratine',
        quadLinked: 'Quad-Linked',
        haywire: 'Haywire (X)',
        luminagen: 'Luminagen',
        transonic: 'Transonic',
        gyroStabilized: 'Gyro-Stabilized',
        vespid: 'Vespid',
        grav: 'Grav',
        gauss: 'Gauss',
        phase: 'Phase',
        tesla: 'Tesla'
    });

    foundry.utils.mergeObject(game.impmal.config.traitHasValue, {
        storm: true,
        haywire: true
    });
});
