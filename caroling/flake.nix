{
  description = "";

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem
    (system: let
      pkgs = import nixpkgs {
        inherit system;
      };
    in {
      devShells.default = pkgs.mkShell rec {
        customPython = pkgs.python310.withPackages (p: with p; [
          mypy
          black
        ]);

        packages = [
          customPython
        ];

        shellHook = "zsh; exit";
      };
    });
}
