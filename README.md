# malexp_FoundryVTT
FoundryVTT module, bringing in the community currated Maledictum Expanded homebrew expansion for the Imperium Maledictum game system.


# Development
**Setup:** Make sure you have npm and nodejs (20+) installed. Run `npm install` in the repository root folder.

## Workflow: Foundry-to-git
1. Make changes in foundry.
2. Lock the compendium once changes are done.
3. Copy foundry ldb file from the module to `build/packs/`
4. Run `npm run ExtractPacks`
5. Review and Commit changes applied to the extracted json files in `packs/...`

## Workflow: Json-to-Foundry
1. Make changes to json files under `packs/...`
2. Run `npm run build` to pack json's into *.ldb file
3. Copy ldb file over the existing one in foundry module/data
4. Start foundry and check changes

## Release
There is a github action hooked to making a new release, that will pack the json content from `packs/...` into ldb(s), adjust the module version in `module.json` and create a release zip artifact.