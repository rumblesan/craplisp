
module Parser
( parse,
  parseExpr,
  subExpr
) where

import Tokeniser ( Token (..) )


parse :: [Token] -> [Token]
parse [] = []
parse tokens = fst $ parseExpr ([], tokens)


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

