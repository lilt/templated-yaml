Pre-Processors
==========================================

.. toctree::
   :maxdepth: 2


The module also supports pre-processors that are placed under the ``tyaml`` key inside the document.  These pre-processors
are removed from the output document.

tyaml.mixins
------------

Includes the values from a separate yaml document, preserving the child's configuration when a conflict is encountered.

*input.yml*

.. code-block:: yaml

   tyaml.mixins:
     - base.yml

   full_name: "Sir {{ name }}"

*base.yml*

.. code-block:: yaml

    name: John Smith

*output.yml*

.. code-block:: yaml

   name: John Smith
   full_name: "Sir John Smith"