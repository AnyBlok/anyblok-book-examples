=====================
AnyBlok book examples
=====================

The anyblok book example source code.

In this master branch, each subdirectories are the content of each branches to
avoid you to get some headkeak using ``git``

So if you want to helps us while fix issue in a chapter, please create
a PR agains the according branch you get the issue.

We have a branch at the end of each chapter to help
book user to start with the expected environment before reading a chapter.

In some special case we provide a dedicated branch that helps to keep
going with boring parts before start a new chapter.

Here the state of each branch

 ========= ========================= ================= ===================
  Chapter   branch name              travis state       coverage
 ========= ========================= ================= ===================
 II_       II_setup-project_         |II-travis|       |II-coverage|
 III-01_   III-01_external-blok_     |III-01-travis|   |III-01-coverage|
 III-02_   III-02_extend-blok_       |III-02-travis|   |III-02-coverage|
 III-03_   III-03_create-model_      |III-03-travis|   |III-03-coverage|
 III-04_   III-04_mixins_            |III-04-travis|   |III-04-coverage|
 III-05_   III-05_link-models_       |III-05-travis|   |III-05-coverage|
 III-06_   III-06_polymorphism_      |III-06-travis|   |III-06-coverage|
 ========= ========================= ================= ===================

maintain
--------

We are using a branch per chapter. A script to helps to rebase each sub branches
on top on the current branch.

Then a dedicated build in the master branch to agregate each branches in a
dedicated subdirectory to avoid gitbook users to be fluent with ``git``


.. warning:

    So, we often use force pushing (``git push --force``)  in this repository


Why
~~~

- To automate change propagation over the book using rebases.
- To provide a linear commit history
- To avoid AnyBlok Book reader's using git over chapters

How
~~~
.. note:

    Begore managing those changes, you should grant push right on this repo. Other
    wise make a PR against the right branch !

In this master branch, a script is provided to automaticly rebase
all child branches according their names. If a rebase has conflict
the script will stop to let you fix it before carry on.

So you can introduce a change somewhere in the book, or merge a PR and it will be
visible in all following branches to recreate a linear history
from where the change were introduce.

* Checkout the branche and introduce your change or merge a PR.
* commit that change
* clone this repo and checkout the master branch in an other directory on
  your computer
* run apply changes in next chapters script to rebase all next chapters
* run test all to run test on each branches
* run push all to push using the force on each branches

To update the master branch, manually restart travis master branch job or
wait a the weekly build !


License
-------

`Free software: Mozilla Public License Version 2.0
<http://mozilla.org/MPL/2.0/>`_


Authors
-------

* Pierre Verkest
* Hugo Quezada
* Jean-Sébastien Suzanne


.. _II: https://anyblok.gitbooks.io/anyblok-book/content/en/02_project/
.. _II_setup-project: https://github.com/AnyBlok/anyblok-book-examples/tree/II_setup-project
.. |II-travis| image:: https://travis-ci.org/AnyBlok/anyblok-book-examples.svg?branch=II_setup-project
    :target: https://travis-ci.org/AnyBlok/anyblok-book-examples
    :alt: Build status
.. |II-coverage| image:: https://coveralls.io/repos/github/AnyBlok/anyblok-book-examples/badge.svg?branch=II_setup-project
    :target: https://coveralls.io/github/AnyBlok/anyblok-book-examples?branch=II_setup-project
    :alt: Coverage

.. _III-01: https://anyblok.gitbooks.io/anyblok-book/content/en/03_blok/01_external_blok.html
.. _III-01_external-blok: https://github.com/AnyBlok/anyblok-book-examples/tree/III-01_external-blok
.. |III-01-travis| image:: https://travis-ci.org/AnyBlok/anyblok-book-examples.svg?branch=III-01_external-blok
    :target: https://travis-ci.org/AnyBlok/anyblok-book-examples
    :alt: Build status
.. |III-01-coverage| image:: https://coveralls.io/repos/github/AnyBlok/anyblok-book-examples/badge.svg?branch=III-01_external-blok
    :target: https://coveralls.io/github/AnyBlok/anyblok-book-examples?branch=III-01_external-blok
    :alt: Coverage

.. _III-02: https://anyblok.gitbooks.io/anyblok-book/content/en/03_blok/02_extend_blok.html
.. _III-02_extend-blok: https://github.com/AnyBlok/anyblok-book-examples/tree/III-02_extend-blok
.. |III-02-travis| image:: https://travis-ci.org/AnyBlok/anyblok-book-examples.svg?branch=III-02_extend-blok
    :target: https://travis-ci.org/AnyBlok/anyblok-book-examples
    :alt: Build status
.. |III-02-coverage| image:: https://coveralls.io/repos/github/AnyBlok/anyblok-book-examples/badge.svg?branch=III-02_extend-blok
    :target: https://coveralls.io/github/AnyBlok/anyblok-book-examples?branch=III-02_extend-blok
    :alt: Coverage

.. _III-03: https://anyblok.gitbooks.io/anyblok-book/content/en/03_blok/03_create_model.html
.. _III-03_create-model: https://github.com/AnyBlok/anyblok-book-examples/tree/III-03_create-model
.. |III-03-travis| image:: https://travis-ci.org/AnyBlok/anyblok-book-examples.svg?branch=III-03_create-model
    :target: https://travis-ci.org/AnyBlok/anyblok-book-examples
    :alt: Build status
.. |III-03-coverage| image:: https://coveralls.io/repos/github/AnyBlok/anyblok-book-examples/badge.svg?branch=III-03_create-model
    :target: https://coveralls.io/github/AnyBlok/anyblok-book-examples?branch=III-03_create-model
    :alt: Coverage

.. _III-04: https://anyblok.gitbooks.io/anyblok-book/content/en/03_blok/04_mixins.html
.. _III-04_mixins: https://github.com/AnyBlok/anyblok-book-examples/tree/III-04_mixins
.. |III-04-travis| image:: https://travis-ci.org/AnyBlok/anyblok-book-examples.svg?branch=III-04_mixins
    :target: https://travis-ci.org/AnyBlok/anyblok-book-examples
    :alt: Build status
.. |III-04-coverage| image:: https://coveralls.io/repos/github/AnyBlok/anyblok-book-examples/badge.svg?branch=III-04_mixins
    :target: https://coveralls.io/github/AnyBlok/anyblok-book-examples?branch=III-04_mixins
    :alt: Coverage

.. _III-05: https://anyblok.gitbooks.io/anyblok-book/content/en/03_blok/05_link_models.html
.. _III-05_link-models: https://github.com/AnyBlok/anyblok-book-examples/tree/III-05_link-models
.. |III-05-travis| image:: https://travis-ci.org/AnyBlok/anyblok-book-examples.svg?branch=III-05_link-models
    :target: https://travis-ci.org/AnyBlok/anyblok-book-examples
    :alt: Build status
.. |III-05-coverage| image:: https://coveralls.io/repos/github/AnyBlok/anyblok-book-examples/badge.svg?branch=III-05_link-models
    :target: https://coveralls.io/github/AnyBlok/anyblok-book-examples?branch=III-05_link-models
    :alt: Coverage

.. _III-06: https://anyblok.gitbooks.io/anyblok-book/content/en/03_blok/06_polymorphism.html
.. _III-06_polymorphism: https://github.com/AnyBlok/anyblok-book-examples/tree/III-06_polymorphism
.. |III-06-travis| image:: https://travis-ci.org/AnyBlok/anyblok-book-examples.svg?branch=III-06_polymorphism
    :target: https://travis-ci.org/AnyBlok/anyblok-book-examples
    :alt: Build status
.. |III-06-coverage| image:: https://coveralls.io/repos/github/AnyBlok/anyblok-book-examples/badge.svg?branch=III-06_polymorphism
    :target: https://coveralls.io/github/AnyBlok/anyblok-book-examples?branch=III-06_polymorphism
    :alt: Coverage
