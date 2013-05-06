
module Parser
( Expression (..),
  parse,
  parseExpr,
  subExpr
) where

import Tokeniser ( Token (..) )

data Expression = Expr [Token] deriving (Show, Eq)


parse :: [Token] -> [Expression]
parse [] = []
parse tokens = map (\(List l) -> Expr l) (fst $ parseExpr ([], tokens))


parseExpr :: ([Token], [Token]) -> ([Token], [Token])
parseExpr (current, []) = (current, [])
parseExpr (current, (i:is))
    | isOpen i = subExpr (current, is)
    | isClose i = (current, is)
    | otherwise = parseExpr (current ++ [i], is)
    where isOpen t = t == OpenParen
          isClose t = t == CloseParen

subExpr :: ([Token], [Token]) -> ([Token], [Token])
subExpr (current, []) = (current, [])
subExpr (output, tokens) =
    let (newExpr, remaining) = parseExpr ([], tokens)
    in parseExpr (output ++ [List newExpr], remaining)

