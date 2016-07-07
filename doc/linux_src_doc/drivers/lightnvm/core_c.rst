.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/lightnvm/core.c

.. _`nvm_submit_ppa_list`:

nvm_submit_ppa_list
===================

.. c:function:: int nvm_submit_ppa_list(struct nvm_dev *dev, struct ppa_addr *ppa_list, int nr_ppas, int opcode, int flags, void *buf, int len)

    submit user-defined ppa list to device. The user must take to free ppa list if necessary.

    :param struct nvm_dev \*dev:
        device

    :param struct ppa_addr \*ppa_list:
        user created ppa_list

    :param int nr_ppas:
        length of ppa_list

    :param int opcode:
        device opcode

    :param int flags:
        device flags

    :param void \*buf:
        data buffer

    :param int len:
        data buffer length

.. _`nvm_submit_ppa`:

nvm_submit_ppa
==============

.. c:function:: int nvm_submit_ppa(struct nvm_dev *dev, struct ppa_addr *ppa, int nr_ppas, int opcode, int flags, void *buf, int len)

    submit PPAs to device. PPAs will automatically be unfolded as single, dual, quad plane PPAs depending on device type.

    :param struct nvm_dev \*dev:
        device

    :param struct ppa_addr \*ppa:
        user created ppa_list

    :param int nr_ppas:
        length of ppa_list

    :param int opcode:
        device opcode

    :param int flags:
        device flags

    :param void \*buf:
        data buffer

    :param int len:
        data buffer length

.. This file was automatic generated / don't edit.

