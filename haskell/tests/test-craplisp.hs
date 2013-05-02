
module Main where

import qualified Tests.Tokeniser ( testTokeniser )
import Data.Monoid
import Test.Framework
import Test.Framework.Providers.HUnit
import Test.HUnit

main :: IO ()
main = defaultMainWithOpts
       [ Tests.Tokeniser.testTokeniser ] mempty

