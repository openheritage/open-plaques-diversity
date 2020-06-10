# open-plaques-diversity
OpenPlaques diversity analysis

# Brief
Following the Black Lives Matter campaign and the toppling of a [statue of Edward Colston](https://en.wikipedia.org/wiki/Statue_of_Edward_Colston) in Bristol the London Mayor's Office is interested in [who is commemorated in London](https://twitter.com/MayorofLondon/status/1270264955200139264]).

OpenPlaques is the largest collection of information on commemorative plaques in the UK (15k records and growing). Open Data is collected along with photographs detailing the inscription, location, and subjects of plaques. Subject records have fields for date of birth, date of death, roles (e.g. policeman, and Fellow of the Royal Society), and gender. Analysis of gender diversity is available on the web site showing a 6:1 male to female imbalance. Plaques have been put up since the early 1900s by a large variety of groups (city councils, local history groups, fan clubs) and imbalances happen through conscious and unconcious biases.

OpenPlaques has no ethnicity field, but it does have a Wikidata ID, and Wikidata has more information that can be used to enhance the data for analysis.

Aims:
1. show the ethnicity diversity (or more likely lack of it) of commemorative plaques in London
2. identify 'bad actors', i.e. people that we might be embarrassed in commemorating because they used to be a slave trader
3. attempt to devise a 'bad actor score' system to give subjects a worthiness rating

# Method
This is a standalone project so that it won't interfere with the main OpenPlaques project.
1. Treat this (and every) project as if you have collaborators
2. Use minimal installed software. Provide a Docker environment with a docker-compose.yml file that has all the required software within it (python, ruby, database, awk, etc.)
3. Use a tool like Github Desktop to pull/push between your local machine and Github
4. Use github issues and project to manage tasks. Work on one issue at a time, assigning it to yourself. Create a branch for each issue. When complete create a pull request, merge into the master branch, and delete the branch.
5. If an issue turns out to be too much to do in on go, or gets held up at the end by something unplanned for cropping up, then consider adding a new issue so that you can complete the current one.
6. Use python or ruby
7. Write tests so that individual examples can be easily re-run, especially when dealing with an anomoly.
8. Consider using tools like Datasette. Would it help, or is it an overhead?
