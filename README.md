# malexp_FoundryVTT
FoundryVTT module, bringing in the community currated Maledictum Expanded homebrew expansion for the Imperium Maledictum game system.

## Status
### Expanded Talents
Contains many more talents, mostly imported from the older FFG 40k titles, expecially from Only War, Rogue Trader and Dark Heresy 1&2.
- [x] Import Data
- [x] Create prerequisite rules
- [ ] Create simple automations
  - [x] Sound Constitution
- [ ] Create complex automations

### Expanded Armouries
Contains many more item options (weapons, armor, drugs, wargear, etc) from various sources.
- [ ] Import Data
- [ ] Automate complex items, like cybernetic and drugs which may require writing effects

# Development
**Setup:** Make sure you have npm and nodejs (20+) installed. Run `npm install` in the repository root folder.

## Workflow: Foundry-to-git
1. Make changes in foundry.
2. Lock the compendium once changes are done.
3. Copy foundry ldb file from the module to `build/packs/`
4. Run `npm run extractPacks`
5. Review and Commit changes applied to the extracted json files in `packs/...`

## Workflow: Json-to-Foundry
1. Make changes to json files under `packs/...`
2. Run `npm run build` to pack json's into *.ldb file
3. Copy ldb file over the existing one in foundry module/data
4. Start foundry and check changes

## Release
There is a github action hooked to making a new release, that will pack the json content from `packs/...` into ldb(s), adjust the module version in `module.json` and create a release zip artifact.