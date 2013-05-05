
module Tests.Parser ( testParser ) where

import Parser
import Test.Framework (Test, testGroup)
import Test.Framework.Providers.HUnit (testCase)
import Test.HUnit hiding (Test)


testParseEmptyList :: Test
testParseEmptyList = testCase "parse an empty list" $ assertEqual
    "Should return an empty list"
    []
    ( parse [] )


testParser :: Test
testParser = testGroup "Parser tests" [testParseEmptyList]

