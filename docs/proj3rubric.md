# Project 2 Rubric


Notes|Self-assement|Evidence|
--------|------|-------|
short release cycles | 0.5 | Evidence in [Releases](https://github.com/TommasU/slash/releases) and [Code Frequency](https://github.com/TommasU/slash/graphs/code-frequency) Short Release cycles were achieved by completing smaller features one at a time instead of a single large feature release. |
workload is spread over the whole team (so one team member is often Xtimes more productive than the others| 0.5 | Evidence in [issue history](https://github.com/TommasU/slash/issues?q=is%3Aissue+is%3Aclosed) & [Contributors](https://github.com/TommasU/slash/graphs/contributors). To provide an even workload between the team, each team member was assign a large feature to implement and support other tasks as needed.|
Docs: why: docs tell a story, motivate the whole thing, deliver a punchline that makes you want to rush out and use the thing|0.5| Evidence in [Readme](https://github.com/TommasU/slash/blob/main/README.md)|
the files CONTRIBUTING .md lists coding standards and lots of tips on how to extend the system without screwing things up|0.5|Evidence in [Contributing](https://github.com/TommasU/slash/blob/main/CONTRIBUTING.md)|
Docs: doco generated , format not ugly| 0.5 | Evidence [Source Code](https://github.com/TommasU/slash/tree/main/src) and Use of Sphinx for documentation generation.|
evidence that the whole team is using the same tools (e.g. config files in the repo, updated by lots of different people)|0.5|Evidence in [requirements.txt](https://github.com/TommasU/slash/blob/main/requirements.txt). The whole team has configured their system using the requirements.txt file.|
evidence that the members of the team are working across multiple places in the code base |0.5| Evidence in [Commit History](https://github.com/TommasU/slash/graphs/commit-activity)|
Docs: what: point descriptions of each class/function (in isolation)| 1 | Function description is included in the code for every function with proper docstring mentioning the function objective, input parameters and return parameters. [Function description](https://github.com/TommasU/slash/blob/main/docs/function_description.md). Individual descriptions can also be found throughout the [source code](https://github.com/TommasU/slash/tree/main/src) with detail descriptions per function/method. |
Number of commits: by different people |0.5| Evidence in [Commit History](https://github.com/TommasU/slash/graphs/commit-activity)|
issues are being closed|1|Evidence in [Closed Issues](https://github.com/TommasU/slash/issues?q=is%3Aissue+is%3Aclosed) & [Project-Slash Phase 3](https://github.com/TommasU/slash/projects/1)|
issues are discussed before they are closed |0.5| Evidence in [issue history](https://github.com/TommasU/slash/issues?q=is%3Aissue+is%3Aclosed). Issues are discussed in Discord channel prior to being closed and merged. Summaries are provided for the main features.| 
Use of syntax checkers.|0.5| Pylint Implementation to check syntax. Evidence in [pylint](https://github.com/TommasU/slash/actions/workflows/pylint.yml)| 
Issues reports: there are many|1| Evidence in [issue history](https://github.com/TommasU/slash/issues)|
Use of code formatters. |0.5|Pylint Implementation to check code format. Evidence in [pylint](https://github.com/TommasU/slash/actions/workflows/pylint.yml) |
Use of style checkers |0.5|Style checker implementation to check code style. Evidence in [Python Style checker](https://github.com/TommasU/slash/actions/workflows/style_checker.yml)|
Docs: short video, animated, hosted on your repo. That convinces people why they want to work on your code. | 0.5 | Evidence in [readme.md](https://github.com/TommasU/slash/blob/main/README.md)|
test cases exist |0.5| Evidence in [tests](https://github.com/TommasU/slash/tree/main/tests) |
Use of code coverage|0.5|Evidence in [code coverage](https://github.com/TommasU/slash/actions/workflows/code_cov.yml)|
other automated analysis tools|0.5| Used automation as [GitHub Actions](https://github.com/TommasU/slash/actions) including travis, Pylint, code coverage, style checker |
test cases:.a large proportion of the issues related to handling failing cases.|0.5|Evidence in [tests](https://github.com/TommasU/slash/tree/main/tests) |
test cases are routinely executed|0.5 | [Github Actions](https://github.com/TommasU/slash/actions)|
Documentation describing how this version improves on the older version|1| Evidence in [readme.md](https://github.com/TommasU/slash/blob/main/README.md) |
  ,,
Q1 - What your software does ,,
"1.1) Does your website and documentation provide a clear, high-level overview of your software? ",YES,
1.2) Does your website and documentation clearly describe the type of user who should use your software? ,YES,
1.3) Do you publish case studies to show how your software has been used by yourself and others? ,NO,
Q2 - Your project's and software's identity ,,
2.1) Is the name of your project/software unique? ,YES,
2.2) Is your project/software name free from trademark violations? ,YES,
Q3 - Availability of your software ,,
3.1) Is your software available as a package that can be deployed without building it? ,NO ,
3.2) Is your software available for free? ,YES,
"3.3) Is your source code publicly available to download, either as a downloadable bundle or via access to a source code repository? ",YES,
"3.4) Is your software hosted in an established, third-party repository ? ",YES,
Q4 - Your software's documentation ,,
 4.1) Is your documentation clearly available on your website or within your software? ,YES,
" 4.2) Does your documentation include a ""quick start"" guide, that provides a short overview of how to use your software with some basic examples of use? ",YES,
" 4.3) If you provide more extensive documentation, does this provide clear, step-by-step instructions on how to deploy and use your software? ",YES,
"4.4) Do you provide a comprehensive guide to all your software’s commands, functions and options? ",YES,
4.5) Do you provide troubleshooting information that describes the symptoms and step-by-step solutions for problems and error messages? ,NO,
"4.6) If your software can be used as a library, package or service by other software, do you provide comprehensive API documentation? ",NO,
4.7) Do you store your documentation under revision control with your source code? ,YES,
"4.8) Do you publish your release history e.g. release data, version numbers, key features of each release etc. on your web site or in your documentation? ",YES,
Q5 - How you support your software ,,
5.1) Does your software describe how a user can get help with using your software? ,YES,
"5.2) Does your website and documentation describe what support, if any, you provide to users and developers? ",YES,
5.3) Does your project have an e-mail address or forum that is solely for supporting users? ,YES,
5.4) Are e-mails to your support e-mail address received by more than one person? ,YES,
5.5) Does your project have a ticketing system to manage bug reports and feature requests? ,YES,
"5.6) Is your project's ticketing system publicly visible to your users, so they can view bug reports and feature requests? ",YES,
Q6 - Your software's maintainability ,,
6.1) Is your software’s architecture and design modular? ,YES, 
6.2) Does your software use an accepted coding standard or convention? ,YES, 
Q7 - Open standards and your software ,,
"7.1) Does your software allow data to be imported and exported using open data formats?  ",YES,
"7.2) Does your software allow communications using open communications protocols? ",YES,
Q8 - Your software's portability ,,
"8.1) Is your software cross-platform compatible? ",YES,
Q9 - Your software and accessibility ,,
9.1) Does your software adhere to appropriate accessibility conventions or standards? ,NO,
9.2) Does your documentation adhere to appropriate accessibility conventions or standards? ,NO,
Q10 - How you manage your source code ,,
10.1) Is your source code stored in a repository under revision control? ,YES,
10.2) Is each source code release a snapshot of the repository? ,YES,
10.3) Are releases tagged in the repository? ,YES,
"10.4) Is there a branch of the repository that is always stable? (i.e. tests always pass, code always builds successfully) ",YES,
10.5) Do you back-up your repository? ,YES,
Q11 - Building and installing your software ,,
11.1) Do you provide publicly-available instructions for building your software from the source code? ,YES,
"11.2) Can you build, or package, your software using an automated tool? ",YES,
11.3) Do you provide publicly available instructions for deploying your software? ,YES,
11.4) Does your documentation list all third-party dependencies? ,YES,
11.5) Does your documentation list the version number for all third-party dependencies? ,YES,
"11.6) Does your software list the web address, and licences for all third-party dependencies and say whether the dependencies are mandatory or ",NO,
"11.7) Can you download dependencies using a dependency management tool or package manager? ",YES,
11.8) Do you have tests that can be run after your software has been built or deployed to show whether the build or deployment has been successful? ,YES,
Q12 - How you test your software ,,
12.1) Do you have an automated test suite for your software? ,NO,
12.2) Do you have a framework to periodically (e.g. nightly) run your tests on the latest version of the source code? ,NO,
"12.3) Do you use continuous integration, automatically running tests whenever changes are made to your source code? ",NO,
12.4) Are your test results publicly visible? ,NO,
12.5) Are all manually run tests documented? ,NO,
Q13 - How you engage with your community ,,
"13.1) Does your project have resources that are regularly updated with information about your software?  ",NO,
13.2)  Does your website state how many projects and users are associated with your project? ,NO,
13.3) Do you provide success stories on your website? ,NO,
13.4) Do you list your important partners and collaborators on your website? ,NO,
13.5) Do you list your project's publications on your website or link to a resource where these are available? ,NO,
13.6) Do you list third-party publications that refer to your software on your website or link to a resource where these are available? ,NO,
13.7) Can users subscribe to notifications to changes to your source code repository? ,YES,
"13.8) If your software is developed as an open source project , do you have a governance model? ",YES,
Q14 - How you manage contributions ,,
"14.1) Do you accept contributions (e.g. bug fixes, enhancements, documentation updates, tutorials) from people who are not part of your project? ",YES,
14.2) Do you have a contributions policy? ,YES,
14.3) Is your contributions' policy publicly available? ,YES,
14.4) Do contributors keep the copyright/IP of their contributions? ,NO,
Q15 - Your software's copyright and licensing ,,
15.1) Does your website and documentation clearly state the copyright owners of your software and documentation? ,YES,
15.2) Does each of your source code files include a copyright statement? ,NO,
15.3) Does your website and documentation clearly state the licence of your software? ,YES,
15.4) Is your software released under an open source licence? ,YES,
15.5) Is your software released under an OSI-approved open-source licence? ,YES,
15.6) Does each of your source code files include a licence header? ,NO,
15.7) Do you have a recommended citation for your software? ,NO,
Q16 - Your plans for the future ,,
"16.1) Does your website or documentation include a project roadmap ? ",YES,
"16.2) Does your website or documentation describe how your project is funded, and the period over which funding is guaranteed? ",NO,
"16.3) Do you make timely announcements of the deprecation of components, APIs, etc.? ",NO,


