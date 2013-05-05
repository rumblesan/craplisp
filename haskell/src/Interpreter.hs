
module Interpreter
(
 VM (..),
 createVm
) where

import qualified Data.Map as Map
import Parser

data VM = VM { symbols :: Map.Map Token Token,
               methods :: [VM -> [Expression] -> Expression],
               scopes :: [Map.Map Token Token],
               funcs :: [Map.Map Token [Expression]]
}

createVm :: VM
createVm = VM { symbols = Map.empty, methods = [], scopes = [], funcs = [] }


