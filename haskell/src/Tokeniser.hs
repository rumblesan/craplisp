module Tokeniser
( Token (..),
  tokenise,
  parse_number,
  parse_symbol,
  parse_string
) where

import Data.Char

data Token = OpenParen
           | CloseParen
           | Symbol String
           | Str String
           | Number Int
           deriving (Show, Eq, Ord)

type ProgramText = String

tokenise :: ProgramText -> [Token]
tokenise program = token_recur (program, [])

token_recur :: (ProgramText, [Token]) -> [Token]
token_recur ([], tokens) = tokens
token_recur (program, tokens)
    | char == '"' = token_recur $ parse_string "" program tokens
    | isSymb char = token_recur $ parse_symbol "" program tokens
    | isNumber char = token_recur $ parse_number "" program tokens
    | char == '(' = token_recur (tail program, tokens ++ [OpenParen])
    | char == ')' = token_recur (tail program, tokens ++ [CloseParen])
    | isSpace char = token_recur (tail program, tokens)
    | otherwise = error $ "Character '" ++ [char] ++ "' is not allowed!"
    where char = head program
          isSymb s = isAlpha s || isSymbol s

parse_number :: String -> ProgramText -> [Token] -> (ProgramText, [Token])
parse_number [] [] _ = ([], [])
parse_number num [] tokens = ([], tokens ++ [Number $ read num])
parse_number num program tokens
    | isNumber char = parse_number (num ++ [char]) (tail program) tokens
    | otherwise = (program, tokens ++ [Number $ read num])
    where char = head program

parse_symbol :: String -> ProgramText -> [Token] -> (ProgramText, [Token])
parse_symbol [] [] _ = ([], [])
parse_symbol symb [] tokens = ([], tokens ++ [Symbol symb])
parse_symbol symb program tokens
    | isSymb char = parse_symbol (symb ++ [char]) (tail program) tokens
    | otherwise = (program, tokens ++ [Symbol symb])
    where char = head program
          isSymb s = isAlpha s || isSymbol s

parse_string :: String -> ProgramText -> [Token] -> (ProgramText, [Token])
parse_string [] [] _ = ([], [])
parse_string str [] tokens = ([], tokens ++ [Str str])
parse_string str program tokens
    | char == '"' && null str  = parse_string str (tail program) tokens
    | char == '"' = (tail program, tokens ++ [Str str])
    | isAlphaNum char = parse_string (str ++ [char]) (tail program) tokens
    | otherwise = (program, tokens ++ [Str str])
    where char = head program

