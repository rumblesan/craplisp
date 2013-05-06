
module Interpreter
(
 VM (..),
 interpret,
 createVm,
 interpretToken,
 interpretExpressions
) where

import qualified Data.Map as Map

import Tokeniser ( Token (..) )
import Parser ( Expression (..) )

type Method = (VM, [Token]) -> (VM, Token)

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

interpret :: [Expression] -> Token
interpret exprs = snd $ interpretExpressions createVm exprs

interpretExpressions :: VM -> [Expression] -> (VM, Token)
interpretExpressions vm exprs =
    let token (Expr t) = List t
    in foldl (\(v, _) e -> interpretToken (v, token e)) (vm, List []) exprs


interpretToken :: (VM, Token) -> (VM, Token)
interpretToken (vm, (List tokens)) =
    let func = head tokens
        args = tail tokens
        method = Map.findWithDefault (error "Could not find method") func (methods vm)
    in method (vm, args)
interpretToken (vm, (Symbol symbol)) = (vm, Symbol symbol)
interpretToken (vm, token) = (vm, token)


mapInterpreting :: VM -> [Token] -> [Token]
mapInterpreting vm tokens = map (\t -> snd $ interpretToken (vm, t)) tokens


method_plus :: Method
method_plus (vm, tokens) =
    let interpreted = mapInterpreting vm tokens
        numbers = map (\(Number x) -> x) interpreted
    in (vm, Number $ sum numbers)

method_sub :: Method
method_sub (vm, tokens) =
    let interpreted = mapInterpreting vm tokens
        numbers = map (\(Number x) -> x) interpreted
    in (vm, Number $ (head numbers) - (sum $ tail numbers))

method_mult :: Method
method_mult (vm, tokens) =
    let interpreted = mapInterpreting vm tokens
        numbers = map (\(Number x) -> x) interpreted
    in (vm, Number $ product numbers)

method_div :: Method
method_div (vm, tokens) =
    let interpreted = mapInterpreting vm tokens
        numbers = map (\(Number x) -> x) interpreted
    in (vm, Number $ (head numbers) `div` (product $ tail numbers))


