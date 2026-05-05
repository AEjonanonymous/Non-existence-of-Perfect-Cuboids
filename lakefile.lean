import Lake
open Lake DSL

package "non-existence-of-perfect-cuboids"

@[default_target]
lean_lib «No Perfect Cuboids»

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.28.0"
