
module Parser
( Expression (..),
  parse,
  parseExpr,
  subExpr
) where

import Tokeniser ( Token )

data Expression = Node Token
                | List [Expression] deriving (Show, Eq)


parse :: [Token] -> [Expression]
parse [] = []
parse tokens = fst $ parseExpr ([], tokens)


parseExpr :: ([Expression], [Token]) -> ([Expression], [Token])
parseExpr (current, []) = (current, [])
parseExpr (current, (i:is))
    | isOpen i = subExpr (current, is)
    | isClose i = (current, is)
    | otherwise = parseExpr (current ++ [Node i], is)
    where isOpen t = t == Token "("
          isClose t = t == Token ")"

subExpr :: ([Expression], [Token]) -> ([Expression], [Token])
subExpr (current, []) = (current, [])
subExpr (output, tokens) =
    let (newExpr, remaining) = parseExpr ([], tokens)
    in parseExpr (output ++ [List newExpr], remaining)

