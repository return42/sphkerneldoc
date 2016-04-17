.. -*- coding: utf-8; mode: rst -*-

=======
setup.c
=======


.. _`setup_priv`:

setup_priv
==========

.. c:function:: void setup_priv ( void)

    Set up privilege protection registers.

    :param void:
        no arguments



.. _`setup_priv.description`:

Description
-----------


Set up privilege protection registers such as TXPRIVEXT to prevent userland
from touching our precious registers and sensitive memory areas.

