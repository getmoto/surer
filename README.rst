surer
=====



.. image:: https://img.shields.io/pypi/dm/surer
   :target: https://pypi.org/project/surer

.. image:: https://github.com/getmoto/surer/workflows/Sure%20Tests/badge.svg
   :target: https://github.com/getmoto/surer/actions?query=workflow%3A%22Sure+Tests%22

.. image:: https://img.shields.io/readthedocs/sure
   :target: https://surer.readthedocs.io/

.. image:: https://img.shields.io/github/license/getmoto/surer?label=Github%20License
   :target: https://github.com/getmoto/surer/blob/master/LICENSE

.. image:: https://img.shields.io/pypi/v/surer
   :target: https://pypi.org/project/surer

.. image:: https://img.shields.io/pypi/l/surer?label=PyPi%20License
   :target: https://pypi.org/project/surer

.. image:: https://img.shields.io/pypi/format/surer
   :target: https://pypi.org/project/surer

.. image:: https://img.shields.io/pypi/status/surer
   :target: https://pypi.org/project/surer

.. image:: https://img.shields.io/pypi/pyversions/surer
   :target: https://pypi.org/project/surer

.. image:: https://img.shields.io/pypi/implementation/surer
   :target: https://pypi.org/project/surer


An idiomatic testing library for python with powerful and flexible assertions, created by `Gabriel Falcão <https://github.com/gabrielfalcao>`_.
Sure's developer experience is inspired and modeled after `RSpec Expectations
<http://rspec.info/documentation/3.5/rspec-expectations/>`_ and
`should.js <https://github.com/shouldjs/should.js>`_.

.. Note::
    This is a fork of Gabriel's library, maintained at `http://github.com/getmoto/surer`. It provides support for more recent Python-versions, but does not differ in functionality.

Installing
----------

.. code:: bash

    $ pip install sure

Documentation
-------------

Available in the `website <https://surer.readthedocs.io/en/latest/>`__ or under the
``docs`` directory.

You can also build the documentation locally using sphinx:

.. code:: bash

    make docs

Here is a tease
---------------

Equality
~~~~~~~~

(number).should.equal(number)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    import sure

    (4).should.be.equal(2 + 2)
    (7.5).should.eql(3.5 + 4)

    (3).shouldnt.be.equal(5)

Assert dictionary and its contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    {'foo': 'bar'}.should.equal({'foo': 'bar'})
    {'foo': 'bar'}.should.have.key('foo').which.should.equal('bar')

"A string".lower().should.equal("a string") also works
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    "Awesome ASSERTIONS".lower().split().should.equal(['awesome', 'assertions'])
