{-  Reversed Binary Numbers
    https://www.spotify.com/us/jobs/tech/reversed-binary/

    Solution by Travis Pennetti -}

import System.Environment -- getArgs
import Data.Char          -- digitToInt
import Numeric            -- showIntAtBase

main = do
  args <- getArgs
  if (not $ null args)
    then print $ (reverseBinary (read (args!!0) :: Int))
    else error "Input is a single positive integer."

reverseBinary :: Int -> Int
reverseBinary n   =   if ((n >= 1) && (n <= 1000000000))
            then binaryToInt 0 (reverse (intToBinary n ""))
            else error "Input is a single positive integer."

-- Precondition: Int is positive and [Char] is initially empty ("")
intToBinary :: Int -> String -> String
intToBinary 0 x   =   x
intToBinary n x   = if n < 0
            then error "Must be a positive integer."
            else intToBinary (n `div` 2) (show (n `mod` 2) ++ x)

-- Precondition: Int is initially zero (0) and String is a bit string
binaryToInt :: Int -> String -> Int
binaryToInt n ""  =   n
binaryToInt n (x:xs)=   case (digitToInt x) of
              (0) ->  binaryToInt n xs
              (1) ->  binaryToInt (n + 2 ^ (length xs)) xs