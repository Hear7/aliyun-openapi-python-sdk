# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkcr.endpoint import endpoint_data

class ListRepositoryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cr', '2018-12-01', 'ListRepository','acr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_RepoName(self):
		return self.get_query_params().get('RepoName')

	def set_RepoName(self,RepoName):
		self.add_query_param('RepoName',RepoName)

	def get_RepoNamespaceName(self):
		return self.get_query_params().get('RepoNamespaceName')

	def set_RepoNamespaceName(self,RepoNamespaceName):
		self.add_query_param('RepoNamespaceName',RepoNamespaceName)

	def get_PageNo(self):
		return self.get_query_params().get('PageNo')

	def set_PageNo(self,PageNo):
		self.add_query_param('PageNo',PageNo)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_RepoStatus(self):
		return self.get_query_params().get('RepoStatus')

	def set_RepoStatus(self,RepoStatus):
		self.add_query_param('RepoStatus',RepoStatus)