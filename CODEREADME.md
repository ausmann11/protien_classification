# FAU Marine Diatoms - Set up local machine

## ATOM (skip if you have a different IDE preference)
1. Use this download link: https://atom.io
2. Open up the application and at the top bar select `Atom` and then `Preferences`. Navigate down to `install`. Search and install packages `Hydrogen`, `python-black` (make sure it is set to toggle on save). Hydrogen allows you to run code interactively in Atom and python black nicely formats code.
  a. In hydrogen make sure to enable the global kernel in settings. Also set the default directory to start the kernel in as the current directory of the file.

## GIT/BITBUCKET
1. Create a bitbucket account https://bitbucket.org/, once finished contact the owner/admins and they can invite you to the bitbucket repo.

### Windows
1. Install git flow using the download link https://git-scm.com/download/win
2. When you are located in the desired folder, run ``git clone https://YOURUSERNAME@bitbucket.org/YOURUSERNAME/fau.git`` it can be copied directly from the bitbucket repo.

### Mac
1. Install homebrew via the terminal ``/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"``
2. Install git flow using ``brew install git-flow``
3. When you are located in the desired folder, run ``git clone https://YOURUSERNAME@bitbucket.org/YOURUSERNAME/fau.git`` it can be copied directly from the bitbucket repo.
  a. If [master] pops up, just hit enter to select all the defaults, from [master] down to version tags[]

## BITBUCKET CONT...
1. Create a folder to house your local version of the code.
2. In the command line, navigate into the folder you created. ``ls`` will display the files/folders in your current location. To move to another folder type ``cd FOLDERNAME``. The folder must be empty to transfer in the code.
3. When you are located in the desired folder, run ``git clone https://YOURUSERNAME@bitbucket.org/YOURUSERNAME/fau.git`` it can be copied directly from the bitbucket repo.
  a. If [master] pops up, just hit enter to select all the defaults, from [master] down to version tags[]
4. Navigate to the FAU folder ``cd fau``
5. Set up git flow by using ``brew install git-flow-avh`` for Mac or on Windows use ``wget -q -O - --no-check-certificate https://raw.github.com/petervanderdoes/gitflow`` and then ``avh/develop/contrib/gitflow-installer.sh install stable | bash``.
6. Start git flow using ``git flow init`` - this only needs to be initialized 1x, after that it always should work.
7. Open the code in atom ``atom .`` (this can always be done to open the application atom)

## CONTRIBUTING CODE
1. To run code, highlight a section of code and hold down `shift`+`enter`
2. Before you create a new branch or open your code, use ``git pull --all`` to make sure you are up to date with the online repository.
2. To modify code, create a separate branch with `git flow feature start NAMEOFBRANCH` - just name it something descriptive to the changes you are making.
3. To save code, use `command`+`s`
4. When you are working on code, you can commit changes you have made, to save them in git. To do this, use ``git commit -am "type a descriptive snippet of what changes or contributions you have made"``.
5. To switch to a different branch, use ``git checkout BRANCHNAME``. For example, to go back to develop -- WHICH IS THE MAIN BRANCH -- ``git checkout develop``. You cannot checkout a new branch without commiting your changes to the code.
6. To put your changes in the online repo, commit changes first and then make sure you are up to date by checking out develop (``git checkout develop``), pulling from the online repo (``git pull --all``) and go back to your branch (``git checkout feature/YOURBRANCHNAME``). Then do ``git push origin``.
7. If there are issues, you may have to rebase. Commit changes, checkout develop, pull the develop, then checkout feature branch, and finally run ``git rebase develop``. Open atom (``atom .``) and then select the version of code in the files throwing errors that you want to keep, it should be highlighted and you can just select `Use Me`. Do ``git rebase --continue`` when you have fixed the conflicts. Once that is done, you should be able to push (``git push origin``).
8. The code will now be in bitbucket! To merge it into develop, first create a pull request so the team can review the code. Go to pull requests in bitbucket, select create pull request, and use the dropdown to select your branch. You can add team members that you want to review your code. Once they have approved, you can select `merge` and then it will be live with develop.

## GENERAL FLOW SUMMARY
PRE GIT: make sure you have the FAU environment installed. FAU environment can be downloaded from google drive. Run ``conda deactive`` if you have an environment running then ``conda env update --name yourenvname --file fauenv.yml``. To use this environment on Jupyter notebooks, use ipykernel ``python -m ipykernel install --user --name yourenvname(i.e. fauenv) --display-name "Python (yourenvname)"``. Keep this environment up to date for group members. Use the conda forge channel ``conda install -c conda-forge conda PACKAGENAMES``. Sometimes conda-forge doesn't contain the necessary package, in which case use ``python -m pip install PACKAGENAME``.

1. Pull - ``git pull --alll`` - update local branch
2. Create Branch - ``git flow feature start NAMEOFFEATUREBRANCH``
3. Code....
4. Commit Code - ``git commit -am "commit message"``
5. Finish branch ``git flow feature finish NAMEOFFEATUREBRANCH``
5. Push Code - ``git flow feature publish`` or ``git push``
6. Create Pull Request - Do in bitbucket
7. Once it approved, merge it in bitbucket

## EXTRA PACKAGES
- This list will be updated as the code base grows, allows us to use new tools in the code.
1. ``pip install boxsdk`` and ``pip install "boxsdk[jwt]"`` allows boxsdk to be installed which makes app.box images accessible directly in python.

## TIPS
- Try to name functions/variables/etc. in an easy to understand manner. To limit the amount of comments that need to be made.
- In the case of unclear code, make sure to comment the process, functions/variables, and what is being done.
- Git processes can also be down in atom (moving between branches and looking at changes for example) at the bottom right.
- If there is something long to document, you can aways create a README.md file to make things more clear (like this file).
- In the terminal, you can access old commands run by hitting the up arrow.
- When you create a folder, before committing you will have to add it using ``git add FOLDERNAME/``
- If you run ``caffeinate`` in the command line it will keep your terminal running even if your monitor shuts down (useful when running models)
- To quit a running process, in the lower left hand corner of Atom `Python 3 | busy` click it and you can interrupt, shutown, or restart the kernel.
- You should only commit when you have functioning code, not just to use it as a save feature. You can always use ``git stash`` if you need to checkout another branch while not ready to commit changes

## USING BOX API
1. Run the auth.py file located in the configuration folder.
2. Login and accept box access when the webpage loads (should boot up when running the auth file).
3. Run scripts, the authorization should be complete.
