
//------------------------------------//

This set of files implements the id match between the Tribunal Superior Eleitoral (TSE) and Congress data on Federal Deputies in Brazil.

Author: Ricardo Dahis
Contact: rdahis@u.northwestern.edu

Last Updated: 02/14/2016

//------------------------------------//


//---------------//
// The Problem
//---------------//

First, TSE provides data on elections in Brazil and the Congress provides data on various variables for each elected deputy. However each institution has its own code for each deputy, and the strings for personal names don't always match. Second, both TSE's and Congress' identification variables (name and code) vary per election cycle (sometimes even within cycle).

//---------------//
// The Solution
//---------------//

This folder contains 4 files, which were created through a matching algorithm and posterior manual checking to maximize the number of matches. All files are normalized (in database-speak). Explanation on how to use below.



//---------------//
// How to Use
//---------------//

1. From TSE data, create a variable called 'candidato', that represents each candidate's name in the given election. Then merge this data set with the file 'candidato_candidato_p.dta'. This will give you a standardized name for candidates across elections.

2. From congress data (on federal amendments in particular), construct the variable 'cd_autor', which consists of the first 4 numbers in each amendment's number. Then merge this data with the file 'cd_autor_cd_autor_p.dta'. This will give you a standardized code for each deputy across years.

3. Merge both datasets (TSE and Congress) with the file 'cd_autor_p - candidato_p.dta'. This will create the link between both institutional IDs.

4. Merge both datasets as you wish, using 'cd_autor_p' or 'candidato_p' as id.



//---------------//
// Observations
//---------------//

1. The file 'cd_autor_p - y_election.dta' maps each 'cd_autor_p' to the years the deputy actually ran for election. This is useful because sometimes you find amendments showing in off-cycle years and you'd like to map to the years when the deputy was actually holding office.

2. Ideally the match should use a candidate's number id, and not its name (since string encoding varies between Windows and Macs). But TSE doesn't provide a number id for candidates, therefore this is still not implemented. The electoral id (titulo de eleitor) could be used, but there are also errors in it across years.

3. The variable 'candidato_p' only exists for candidates that eventually were elected and have records in Congress data. Creating this variable for all election candidates would be very time-consuming and in fact useless.

4. Many elected deputies end up leaving office before the end of the cycle, and substitutes enter in their place (given the Brazilian Open List Proportional Representation system). This match includes data on these substitutes only up to those who eventually created amendments. It also doesn't identify the specific year the substitutes took office.






