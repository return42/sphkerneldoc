.. -*- coding: utf-8; mode: rst -*-

===========
cryp_irqp.h
===========


.. _`__cryp_irqp_h_`:

__CRYP_IRQP_H_
==============

.. c:function:: __CRYP_IRQP_H_ ()

    Ericsson SA 2010



.. _`__cryp_irqp_h_.author`:

Author
------

Niklas Hernaeus <niklas.hernaeus\ ``stericsson``\ .com> for ST-Ericsson.



.. _`__cryp_irqp_h_.author`:

Author
------

Niklas Hernaeus <niklas.hernaeus\ ``stericsson``\ .com> for ST-Ericsson.



.. _`__cryp_irqp_h_.author`:

Author
------

Niklas Hernaeus <niklas.hernaeus\ ``stericsson``\ .com> for ST-Ericsson.



.. _`__cryp_irqp_h_.author`:

Author
------

Niklas Hernaeus <niklas.hernaeus\ ``stericsson``\ .com> for ST-Ericsson.



.. _`__cryp_irqp_h_.author`:

Author
------

Niklas Hernaeus <niklas.hernaeus\ ``stericsson``\ .com> for ST-Ericsson.



.. _`__cryp_irqp_h_.license-terms`:

License terms
-------------

GNU General Public License (GPL) version 2



.. _`cryp_register`:

struct cryp_register
====================

.. c:type:: cryp_register

    


.. _`cryp_register.definition`:

Definition
----------

.. code-block:: c

  struct cryp_register {
  };


.. _`cryp_register.members`:

Members
-------




.. _`cryp_register.description`:

Description
-----------

``cr``                        - Configuration register
``status``                - Status register
``din``                        - Data input register
``din_size``                - Data input size register
``dout``                - Data output register
``dout_size``                - Data output size register
``dmacr``                - Dma control register
``imsc``                - Interrupt mask set/clear register
``ris``                        - Raw interrupt status
``mis``                        - Masked interrupt statu register
``key_1_l``                - Key register 1 L
``key_1_r``                - Key register 1 R
``key_2_l``                - Key register 2 L
``key_2_r``                - Key register 2 R
``key_3_l``                - Key register 3 L
``key_3_r``                - Key register 3 R
``key_4_l``                - Key register 4 L
``key_4_r``                - Key register 4 R
``init_vect_0_l``        - init vector 0 L
``init_vect_0_r``        - init vector 0 R
``init_vect_1_l``        - init vector 1 L
``init_vect_1_r``        - init vector 1 R
``cryp_unused1``        - unused registers
``itcr``                - Integration test control register
``itip``                - Integration test input register
``itop``                - Integration test output register
``cryp_unused2``        - unused registers
``periphId0``                - FE0 CRYP Peripheral Identication Register
``periphId1``                - FE4
``periphId2``                - FE8
``periphId3``                - FEC
``pcellId0``                - FF0  CRYP PCell Identication Register
``pcellId1``                - FF4
``pcellId2``                - FF8
``pcellId3``                - FFC

