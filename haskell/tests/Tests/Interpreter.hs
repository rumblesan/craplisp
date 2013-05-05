
module Tests.Interpreter ( testInterpreter ) where

import Interpreter
import Tokeniser
import Test.Framework (Test, testGroup)
import Test.Framework.Providers.HUnit (testCase)
import Test.HUnit hiding (Test)


testInterpretBasic :: Test
testInterpretBasic = testCase "interpret a single token" $ assertEqual
    "Should return a single token"
    (Number 5)
    ( interpret (Number 5) )

testAddition :: Test
testAddition = testCase "interpret a basic program" $ assertEqual
    "Should return the sum of the tokens"
    (Number 8)
    ( interpret (List [Symbol "+", Number 2, Number 3, Number 3]) )

testSubtraction :: Test
testSubtraction = testCase "interpret a basic program" $ assertEqual
    "Should return the first token minus the rest"
    (Number 4)
    ( interpret (List [Symbol "-", Number 10, Number 3, Number 3]) )

testDivision :: Test
testDivision = testCase "interpret a basic program" $ assertEqual
    "Should return the first token divided by the rest"
    (Number 2)
    ( interpret (List [Symbol "/", Number 100, Number 10, Number 5]) )

testMultiplication :: Test
testMultiplication = testCase "interpret a basic program" $ assertEqual
    "Should return the product of the tokens"
    (Number 24)
    ( interpret (List [Symbol "*", Number 2, Number 3, Number 4]) )



testInterpreter :: Test
testInterpreter = testGroup "Parser tests" [testInterpretBasic,
                                            testAddition,
                                            testSubtraction,
                                            testDivision,
                                            testMultiplication]

