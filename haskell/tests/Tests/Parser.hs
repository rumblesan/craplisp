
module Tests.Parser ( testParser ) where

import Tokeniser ( Token (..) )
import Parser
import Test.Framework (Test, testGroup)
import Test.Framework.Providers.HUnit (testCase)
import Test.HUnit hiding (Test)


testParseEmptyList :: Test
testParseEmptyList = testCase "parse an empty list" $ assertEqual
    "Should return an empty list"
    []
    ( parse [] )

testParseBasicProgram :: Test
testParseBasicProgram = testCase "parse a basic program" $ assertEqual
    "Should return an Expression containing a list of Tokens"
    [Expr [Symbol "+", Number 1, Number 4]]
    ( parse [OpenParen, Symbol "+", Number 1, Number 4, CloseParen] )


testParser :: Test
testParser = testGroup "Parser tests" [testParseEmptyList, testParseBasicProgram]

