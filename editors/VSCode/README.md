# Visual Studio Code configuration files

> **These settings only have effect with the C/C++ extension installed.**

### Setup

Place the `.vscode` folder at the root of the Tsuru repository folder, aka what should be called the `files` folder if your setup is correct.

#### Check the following lines containing file paths, and change them to the correct paths on your system if needed:
- [Compiler Path](https://github.com/Luminyx1/Tsuru-Assets/blob/main/editors/VSCode/.vscode/c_cpp_properties.json#L17) - Doesn't have to be Cygwin g++, any compiler which supports **linux-gcc-x86** intellisense mode should work.
- [GHS Headers Paths](https://github.com/Luminyx1/Tsuru-Assets/blob/main/editors/VSCode/.vscode/settings.json#L10-L16) - Only change the `C:/ghs/multi5327` part of all 5 paths.

#### You may already have a `.vscode` folder, if you do:
- If `c_cpp_properties.json` exists, delete it and replace with the one from here.
- If `settings.json` exists, manually copy and paste the keys from the one from here into it, merging with your existing settings.
  - Make sure to not leave duplicate keys and if there are, the ones from here should take priority and the existing should be removed.
