.. -*- coding: utf-8; mode: rst -*-

=====
llc.h
=====


.. _`llc_sap`:

struct llc_sap
==============

.. c:type:: llc_sap

    Defines the SAP component


.. _`llc_sap.definition`:

Definition
----------

.. code-block:: c

  struct llc_sap {
  };


.. _`llc_sap.members`:

Members
-------




.. _`llc_sap.description`:

Description
-----------


``station`` - station this sap belongs to
``state`` - sap state
``p_bit`` - only lowest-order bit used
``f_bit`` - only lowest-order bit used
``laddr`` - SAP value in this 'lsap'
``node`` - entry in station sap_list
``sk_list`` - LLC sockets this one manages

