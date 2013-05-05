
module Main where

import Tests.Tokeniser ( testTokeniser )
import Tests.Parser ( testParser )

import Test.Framework (Test, defaultMain)

main :: IO ()
main = defaultMain tests

tests :: [Test]
tests = [testTokeniser, testParser]

