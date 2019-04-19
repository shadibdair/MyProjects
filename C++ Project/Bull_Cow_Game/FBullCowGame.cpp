#pragma once
#include "FBullCowGame.h"
#include <map>

// to make the syntax Unreal friendly
#define TMap std::map

FBullCowGame::FBullCowGame() { Reset(); } // defualt constrctor

int32 FBullCowGame::GetCurrentTry() const {return MyCurrentTry;}
int32 FBullCowGame::GetHiddenWordLengtgh() const {return MyHiddenWord.length();}
bool FBullCowGame::IsgameWon() const {return bGameIsWon;}

int32 FBullCowGame::GetMaxTries() const 
{ 
	TMap<int32, int32> WordLengthToMaxTries{ {3,4},{4,7},{5,10},{6,16},{7,20} };
	return WordLengthToMaxTries[MyHiddenWord.length()];
}


void FBullCowGame::Reset()
{
	const FString HIIDEN_WORD = "planet"; // this MUST be an isogram
	MyHiddenWord = HIIDEN_WORD;

	MyCurrentTry = 1;
	bGameIsWon = false;
	return;
}

EGuessStatus FBullCowGame::CheckGuessValidity(FString Guess) const
{
	if (!IsIsogram(Guess))// if the guess isn't an isogram,
	{
		return EGuessStatus::Not_Isogram; 
	}
	else if(!IsLowercase(Guess))// if the guess isn't all lowercase.
	{
		return EGuessStatus::Not_Lowercase;
	}
	else if (Guess.length() != GetHiddenWordLengtgh())	// if the guess length is wrong
	{
		return EGuessStatus::Wrong_Length;
	}
	else 
	{
		return EGuessStatus::OK;
	}

}

// receives a VALID guess, incriments turn, and return count
FBullCowCount FBullCowGame::SubmitValidGuess(FString Guess)
{
	// incriment the turn number
	MyCurrentTry++;

	//setup a return variable
	FBullCowCount BullCowCount;

	// loop through all letters in the guess
	int32 WordLength = MyHiddenWord.length();
	for (int32 MHWChar = 0; MHWChar < WordLength; MHWChar++)
	{
		//compare letters against the hiiden word
		for (int32 GChar = 0; GChar < WordLength; GChar++) 
		{
			// if they match then
			if (Guess[GChar] == MyHiddenWord[MHWChar])
			{
				
				if (MHWChar == GChar) // if they're in the same placce
				{
					BullCowCount.Bulls++; // incriment bulls
				}
				else
				{
					BullCowCount.Cows++; // must be a cows 
				}
			}
		}
	}
	if (BullCowCount.Bulls == WordLength)
	{
		bGameIsWon = true;
	}
	else {
		bGameIsWon = false;
	}
	return BullCowCount;
}

bool FBullCowGame::IsIsogram(FString Word) const
{
	// treat 0 and 1 letter words as isograms
	if (Word.length() <= 1) { return true; }

	TMap<char, bool> LetterSeen; // setup our mapp
	for (auto Letter : Word) // for all letter of the word
	{
		Letter = tolower(Letter); // handle mixed case
		if (LetterSeen[Letter]) {// if the letter is in the map
			return false; // we do NOT have an isogram
		}
		else {
			LetterSeen[Letter] = true; // add the letter to the map as seen
		}
	}
	return true; // for example in cases where /0 is entered
}

bool FBullCowGame::IsLowercase(FString Word) const
{
	for (auto Letter : Word)
	{
		if (!islower(Letter))// if not a lowercase letter
		{
			return false;
		}
	}
	return true;
}
