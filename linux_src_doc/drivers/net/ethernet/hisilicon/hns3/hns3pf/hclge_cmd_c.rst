.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns3/hns3pf/hclge_cmd.c

.. _`hclge_cmd_send`:

hclge_cmd_send
==============

.. c:function:: int hclge_cmd_send(struct hclge_hw *hw, struct hclge_desc *desc, int num)

    send command to command queue

    :param struct hclge_hw \*hw:
        pointer to the hw struct

    :param struct hclge_desc \*desc:
        prefilled descriptor for describing the command

    :param int num:
        the number of descriptors to be sent

.. _`hclge_cmd_send.description`:

Description
-----------

This is the main send command for command queue, it
sends the queue, cleans the queue, etc

.. This file was automatic generated / don't edit.

