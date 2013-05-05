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
           | Number Int
           deriving (Show, Eq, Ord)

tokenise :: String -> [String]
tokenise program = token_recur (program, [])

token_recur :: (String, [String]) -> [String]
token_recur ([], tokens) = tokens
token_recur (program, tokens)
    | char == '"' = token_recur $ parse_string "" program tokens
    | isSymb char = token_recur $ parse_symbol "" program tokens
    | isNumber char = token_recur $ parse_number "" program tokens
    | char == '(' = token_recur (tail program, tokens ++ [[char]])
    | char == ')' = token_recur (tail program, tokens ++ [[char]])
    | isSpace char = token_recur (tail program, tokens)
    | otherwise = error "Shouldn't be anything else"
    where char = head program
          isSymb s = isAlpha s || isSymbol s

parse_number :: String -> String -> [String] -> (String, [String])
parse_number num [] tokens = ([], tokens ++ [num])
parse_number num program tokens
    | isNumber char = parse_number (num ++ [char]) (tail program) tokens
    | otherwise = (program, tokens ++ [num])
    where char = head program

parse_symbol :: String -> String -> [String] -> (String, [String])
parse_symbol symb [] tokens = ([], tokens ++ [symb])
parse_symbol symb program tokens
    | isSymb char = parse_symbol (symb ++ [char]) (tail program) tokens
    | otherwise = (program, tokens ++ [symb])
    where char = head program
          isSymb s = isAlpha s || isSymbol s

parse_string :: String -> String -> [String] -> (String, [String])
parse_string str [] tokens = ([], tokens ++ [str])
parse_string str program tokens
    | char == '"' && null str  = parse_string str (tail program) tokens
    | char == '"' = (tail program, tokens ++ [str])
    | isAlphaNum char = parse_string (str ++ [char]) (tail program) tokens
    | otherwise = (program, tokens ++ [str])
    where char = head program

