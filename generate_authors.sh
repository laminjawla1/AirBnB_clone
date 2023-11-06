#!/bin/bash
git log --format='%aN <%aE>' | sort -uf > AUTHORS