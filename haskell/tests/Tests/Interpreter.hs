
module Tests.Interpreter ( testInterpreter ) where

import Parser
import Interpreter
import Tokeniser
import Test.Framework (Test, testGroup)
import Test.Framework.Providers.HUnit (testCase)
import Test.HUnit hiding (Test)


testAddition :: Test
testAddition = testCase "interpret a basic program" $ assertEqual
    "Should return the sum of the tokens"
    (Number 8)
    ( interpret [Expr [Symbol "+", Number 2, Number 3, Number 3]] )

testSubtraction :: Test
testSubtraction = testCase "interpret a basic program" $ assertEqual
    "Should return the first token minus the rest"
    (Number 4)
    ( interpret [Expr [Symbol "-", Number 10, Number 3, Number 3]] )

testDivision :: Test
testDivision = testCase "interpret a basic program" $ assertEqual
    "Should return the first token divided by the rest"
    (Number 2)
    ( interpret [Expr [Symbol "/", Number 100, Number 10, Number 5]] )

testMultiplication :: Test
testMultiplication = testCase "interpret a basic program" $ assertEqual
    "Should return the product of the tokens"
    (Number 24)
    ( interpret [Expr [Symbol "*", Number 2, Number 3, Number 4]] )



testInterpreter :: Test
testInterpreter = testGroup "Parser tests" [testAddition,
                                            testSubtraction,
                                            testDivision,
                                            testMultiplication]

