
module Tests.Tokeniser ( testTokeniser ) where

import Tokeniser ( tokenise, parse_number, parse_symbol, parse_string )
import Test.HUnit

testParseEmptyNumber :: Test
testParseEmptyNumber = TestCase $ assertEqual
    "Should get empty string and list with a list from empty input"
    ("", [[]])
    ( parse_number "" "" [] )

testParseNumber :: Test
testParseNumber = TestCase $ assertEqual
    "Should get empty string and list with a number string in"
    ("", ["1234"])
    ( parse_number "" "1234" [] )

testParseNumberFollowedByChars :: Test
testParseNumberFollowedByChars = TestCase $ assertEqual
    "Should get only initial number chars and list with a number string in"
    ("abcdef456", ["1234"])
    ( parse_number "" "1234abcdef456" [] )


testParseSymbol :: Test
testParseSymbol = TestCase $ assertEqual
    "Should get string of spaces and list with a symbol string in"
    (" ", ["++"])
    ( parse_symbol "" "++ " [] )


testParseString :: Test
testParseString = TestCase $ assertEqual
    "Should get string of spaces and list with a string in"
    ("  ", ["string"])
    ( parse_string "" "\"string\"  " [] )


testTokeniseProgram :: Test
testTokeniseProgram = TestCase $ assertEqual
    "Should get a list of tokens"
    ["(", "+", "34673", "(", "double", "903245", ")", ")"]
    ( tokenise " ( + 34673 ( double 903245 ) )  " )


testTokeniser :: Test
testTokeniser = TestList [testParseEmptyNumber,
                          testParseNumber,
                          testParseNumberFollowedByChars,
                          testParseSymbol,
                          testParseString,
                          testTokeniseProgram]

