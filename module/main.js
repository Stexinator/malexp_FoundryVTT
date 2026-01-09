Hooks.on('init', () => {
    foundry.utils.mergeObject(game.impmal.config.disciplines, {
        nurglitePowers: 'Nurglite Powers'
    });
});
