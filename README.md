# Tsuru-Assets
Assets repository for the [Tsuru](https://github.com/Luminyx1/Tsuru-Dev) project.

## Repository Structure
- `MiyamotoPatch/`: Relevant [Miyamoto Level Editor](https://github.com/aboood40091/Miyamoto) patches and spritedata.
  - `Tsuru/`: The main Miyamoto patch of the project. Contains spritedata of custom sprites. ([Download](https://github.com/Luminyx1/Tsuru-Assets/releases/tag/latest-miyamoto-patch))

- `editors/`: Development workspace configuration files for code editors intellisense and other features.
  - `VSCode/`: Workspace configuration files for [VS Code](https://code.visualstudio.com/). This is the only editor we (Tsuru maintainers) will support, but PRs for config files of other editors are welcome.

- `game/`: A partial representation of the NSMBU v1.3 filesystem containing only custom assets of the project, to be easily merged with the filesystem of a clean base ROM.
