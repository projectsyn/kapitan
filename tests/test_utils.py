#!/usr/bin/env python3

# Copyright 2019 The Kapitan Authors
# SPDX-FileCopyrightText: 2020 The Kapitan Authors <kapitan-admins@googlegroups.com>
#
# SPDX-License-Identifier: Apache-2.0

"utils tests"

import unittest
import os
import tempfile
import glob
import shutil

from kapitan.utils import copy_tree, directory_hash, SafeCopyError

TEST_PWD = os.getcwd()
TEST_RESOURCES_PATH = os.path.join(os.getcwd(), "tests/test_resources")
TEST_DOCKER_PATH = os.path.join(os.getcwd(), "examples/docker/")
TEST_TERRAFORM_PATH = os.path.join(os.getcwd(), "examples/terraform/")
TEST_KUBERNETES_PATH = os.path.join(os.getcwd(), "examples/kubernetes/")


class CopyTreeTest(unittest.TestCase):
    "Test copy_tree function"

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        
        
    def test_copy_dir(self):
        original = set(glob.iglob(f"{TEST_KUBERNETES_PATH}/*", recursive=True))
        copied = copy_tree(TEST_KUBERNETES_PATH, self.temp_dir)
        self.assertEqual(len(copied), len(original))

        original_hash = directory_hash(TEST_KUBERNETES_PATH)
        copied_hash = directory_hash(self.temp_dir)
        self.assertEqual(copied_hash, original_hash)


    def test_validate_copy_dir(self):
        with self.assertRaises(SafeCopyError):
            copy_tree("non_existent_dir", self.temp_dir)
            
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
        