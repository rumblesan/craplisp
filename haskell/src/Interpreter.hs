
module Interpreter
(
 VM (..),
 interpret,
 createVm,
 interpretExpression
) where

import qualified Data.Map as Map

import Tokeniser ( Token (..) )

type Method = VM -> [Token] -> Token

data VM = VM { symbols :: Map.Map Token Token,
               methods :: Map.Map Token Method,
               scopes :: [Map.Map Token Token],
               funcs :: [Map.Map Token Token]
}

--currentScope :: VM -> Map.Map Token Token
--currentScope VM { scopes=[] } = Map.empty
--currentScope VM { scopes=localscopes } = head localscopes

createVm :: VM
createVm = VM { symbols = Map.empty, methods = createMethodMap, scopes = [], funcs = [] }


createMethodMap :: Map.Map Token Method
createMethodMap = Map.fromList [ (Symbol "+", method_plus),
                                 (Symbol "-", method_sub),
                                 (Symbol "*", method_mult),
                                 (Symbol "/", method_div)
                               ]

interpret :: Token -> Token
interpret = interpretExpression $ createVm

interpretExpression :: VM -> Token -> Token
interpretExpression vm (List tokens) =
    let func = head tokens
        args = tail tokens
        method = Map.findWithDefault (error "Could not find method") func (methods vm)
    in method vm args
interpretExpression _ (Symbol symbol) = Symbol symbol
interpretExpression _ token = token


method_plus :: Method
method_plus vm expressions =
    let interpreted = map (interpretExpression vm) expressions
        numbers = map (\(Number x) -> x) interpreted
    in Number $ sum numbers

method_sub :: Method
method_sub vm expressions =
    let interpreted = map (interpretExpression vm) expressions
        numbers = map (\(Number x) -> x) interpreted
    in Number $ (head numbers) - (sum $ tail numbers)

method_mult :: Method
method_mult vm expressions =
    let interpreted = map (interpretExpression vm) expressions
        numbers = map (\(Number x) -> x) interpreted
    in Number $ product numbers

method_div :: Method
method_div vm expressions =
    let interpreted = map (interpretExpression vm) expressions
        numbers = map (\(Number x) -> x) interpreted
    in Number $ (head numbers) `div` (product $ tail numbers)


