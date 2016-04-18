.. -*- coding: utf-8; mode: rst -*-

.. _xref_table_concerns:

===============
Creating tables
===============


Simple tables
=============

.. code-block:: rst

  =====  =====  ======
     Inputs     Output
  ------------  ------
    A      B    A or B
  =====  =====  ======
         False
         True
  --------------------
  True   False  True
  False  True   True
  =====  =====  ======

Rendered as:

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False
--------------------
True
--------------------
True   False  True
False  True   True
=====  =====  ======


Grid tables
===========

.. code-block:: rst

   +------------+------------+-----------+
   | Header 1   | Header 2   | Header 3  |
   +============+============+===========+
   | body row 1 | column 2   | column 3  |
   +------------+------------+-----------+
   | body row 2 | Cells may span columns.|
   +------------+------------+-----------+
   | body row 3 | Cells may  | - Cells   |
   +------------+ span rows. | - contain |
   | body row 4 |            | - blocks. |
   +------------+------------+-----------+

Rendered as:

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+


Nested Tables
=============

Nested tables are ugly, don't use them. This is only for test, how it would be
rendered.

.. code-block:: rst

   +-----------+----------------------------------------------------+
   | W/NW cell | N/NE cell                                          |
   |           +-------------+--------------------------+-----------+
   |           | W/NW center | N/NE center              | E/SE cell |
   |           |             +------------+-------------+           |
   |           |             | +--------+ | E/SE center |           |
   |           |             | | nested | |             |           |
   |           |             | +--------+ |             |           |
   |           |             | | table  | |             |           |
   |           |             | +--------+ |             |           |
   |           +-------------+------------+             |           |
   |           | S/SE center              |             |           |
   +-----------+--------------------------+-------------+           |
   | S/SW cell                                          |           |
   +----------------------------------------------------+-----------+

Rendered as:

+-----------+----------------------------------------------------+
| W/NW cell | N/NE cell                                          |
|           +-------------+--------------------------+-----------+
|           | W/NW center | N/NE center              | E/SE cell |
|           |             +------------+-------------+           |
|           |             | +--------+ | E/SE center |           |
|           |             | | nested | |             |           |
|           |             | +--------+ |             |           |
|           |             | | table  | |             |           |
|           |             | +--------+ |             |           |
|           +-------------+------------+             |           |
|           | S/SE center              |             |           |
+-----------+--------------------------+-------------+           |
| S/SW cell                                          |           |
+----------------------------------------------------+-----------+


List tables
===========

.. code-block:: rst

   .. list-table::
      :header-rows: 1
      :stub-columns: 1

      * - ..
        - head col 1
        - head col 2

      * - stub col row 1
        - column
          - column

      * - stub col row 2
        - column
        - column

      * - stub col row 3
        - column
        - column

Rendered as:

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - ..
     - head col 1
     - head col 2

   * - stub col row 1
     - column
     - column

   * - stub col row 2
     - column
     - column

   * - stub col row 3
     - column
     - column


CSV table
=========

.. code-block:: rst

   .. csv-table::
      :header: , Header1, Header2
      :widths: 15, 10, 30
      :stub-columns: 1
      :file: csv_table.txt

Content of file ``csv_table.txt``:

.. literalinclude:: csv_table.txt

Rendered as:

.. csv-table::
   :header: , Header1, Header2
   :widths: 15, 10, 30
   :stub-columns: 1
   :file: csv_table.txt



raw HTML tables
===============

If HTML is the only format you want to render, you could use a raw-import of a
HTML table markup. But be aware, this breaks the separation of *presentation from
content*. HTML-Tables are only rendered within a HTML output.

.. code-block:: html

   <div class="wy-table-responsive">
   <table class="docutils">
     <thead>
       <tr style="font-weight: bold;">
	 <td>Owner Module/Drivers</td>
	 <td>Group</td>
	 <td>Property Name</td>
	 <td>Type</td>
	 <td>Property Values</td>
	 <td>Object attached</td>
	 <td>Description/Restrictions</td>
       </tr>
     </thead>
     <tbody>
       <tr>
	 <td rowspan="4">DRM</td>
	 <td>Generic</td>
	 <td>"rotation"</td>
	 <td>BITMASK</td>
	 <td>{ 0, "rotate-0" }, { 1, "rotate-90" }, { 2, "rotate-180" }, { 3,
	   "rotate-270" }, { 4, "reflect-x" }, { 5, "reflect-y" }</td>
	 <td>CRTC, Plane</td>
	 <td>rotate-(degrees) rotates the image by the specified amount in
	  degrees in counter clockwise direction. reflect-x and reflect-y
	  reflects the image along the specified axis prior to rotation</td>
       </tr>

       <tr>
	 <td rowspan="3">Connector</td>
	 <td>"EDID"</td>
	 <td>BLOB | IMMUTABLE</td>
	 <td>0</td>
	 <td>Connector</td>
	 <td>Contains id of edid blob ptr object.</td>
       </tr>

       <tr>
	 <td>"DPMS"</td>
	 <td>ENUM</td>
	 <td>{ "On", "Standby", "Suspend", "Off" }</td>
	 <td>Connector</td>
	 <td>Contains DPMS operation mode value.</td>
       </tr>

       <tr>
	 <td>"PATH"</td>
	 <td>BLOB | IMMUTABLE</td>
	 <td>0</td>
	 <td>Connector</td>
	 <td>Contains topology path to a connector.</td>
       </tr>
     </tbody>
   </table>
   </div>



.. raw:: html

   <div class="wy-table-responsive">
   <table class="docutils">
     <thead>
       <tr style="font-weight: bold;">
	 <td>Owner Module/Drivers</td>
	 <td>Group</td>
	 <td>Property Name</td>
	 <td>Type</td>
	 <td>Property Values</td>
	 <td>Object attached</td>
	 <td>Description/Restrictions</td>
       </tr>
     </thead>
     <tbody>
       <tr>
	 <td rowspan="4">DRM</td>
	 <td>Generic</td>
	 <td>"rotation"</td>
	 <td>BITMASK</td>
	 <td>{ 0, "rotate-0" }, { 1, "rotate-90" }, { 2, "rotate-180" }, { 3,
	   "rotate-270" }, { 4, "reflect-x" }, { 5, "reflect-y" }</td>
	 <td>CRTC, Plane</td>
	 <td>rotate-(degrees) rotates the image by the specified amount in
	  degrees in counter clockwise direction. reflect-x and reflect-y
	  reflects the image along the specified axis prior to rotation</td>
       </tr>

       <tr>
	 <td rowspan="3">Connector</td>
	 <td>"EDID"</td>
	 <td>BLOB | IMMUTABLE</td>
	 <td>0</td>
	 <td>Connector</td>
	 <td>Contains id of edid blob ptr object.</td>
       </tr>

       <tr>
	 <td>"DPMS"</td>
	 <td>ENUM</td>
	 <td>{ "On", "Standby", "Suspend", "Off" }</td>
	 <td>Connector</td>
	 <td>Contains DPMS operation mode value.</td>
       </tr>

       <tr>
	 <td>"PATH"</td>
	 <td>BLOB | IMMUTABLE</td>
	 <td>0</td>
	 <td>Connector</td>
	 <td>Contains topology path to a connector.</td>
       </tr>
     </tbody>
   </table>
   </div>

Miscellaneous & thougth
=======================

* `Emacs Table Mode`_
* `Online Tables Generator`_

Internal the docutils uses a representation according to the `OASIS XML Exchange
Table Model`_ (same as DocBook).  It would be nice to have a `directive
<http://www.sphinx-doc.org/en/stable/extdev/tutorial.html#the-directive-classes>`_
``xml-table`` (like ``csv-table``) wich reads *OASIS XML Exchange Table*
data. This directive might be a big step forward to migrate the massive table
based DocBook documentation from Kernel-docs.  `rusty
<https://pypi.python.org/pypi/rusty/>`_ brings some directives (I haven't tested
yet).


.. include:: refs.txt
