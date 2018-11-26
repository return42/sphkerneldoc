.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/bpf/lpm_trie.c

.. _`longest_prefix_match`:

longest_prefix_match
====================

.. c:function:: size_t longest_prefix_match(const struct lpm_trie *trie, const struct lpm_trie_node *node, const struct bpf_lpm_trie_key *key)

    determine the longest prefix

    :param trie:
        The trie to get internal sizes from
    :type trie: const struct lpm_trie \*

    :param node:
        The node to operate on
    :type node: const struct lpm_trie_node \*

    :param key:
        The key to compare to \ ``node``\ 
    :type key: const struct bpf_lpm_trie_key \*

.. _`longest_prefix_match.description`:

Description
-----------

Determine the longest prefix of \ ``node``\  that matches the bits in \ ``key``\ .

.. This file was automatic generated / don't edit.

