
import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

//Import and Use Axios


import apiRoutes from '@/js/api-routes';

export const Users = {
	namespace: true,
	state: {
		//User and Employee Personal Data
		userProfile: {},
		//All Users based on Logged in User

		//Own Business Employees
		userList: [],
		companyFilteredEmployeeList: [],

		//Selected Business Employees
		selectedUserList: [],
	},
	mutations: {
		SET_USER_PROFILE(state, payload) {
			state.userProfile = payload;
		},
		PUSH_NEW_USER(state, payload) {
      state.userList.push(payload);
		},
		

		SET_USER_LIST(state, payload) {
			console.log("SET_EMPLOYEE_LIST payload", payload);
			state.employeeList = payload;
		},
		PUSH_NEW_EMPLOYEE(state, payload) {
			state.employeeList.push(payload);
		},
			
		CLEAR_USER_DATA(state, payload) {
			state.userProfile = {};
		},
		SET_SELECTED_EMPLOYEE_PROFILE(state, payload) {
      state.selectedPartnerProfile = payload;
    },
    UPDATE_EMPLOYEE_PROFILE() {
      console.log('payload', payload);
      let listIndex = state.employeeList.findIndex(elem => elem.id === payload.id);
      state.employeeList.slice(listIndex, 1);
      state.employeeList.splice(listIndex, 1, payload);
      console.log('state.employeeList', state.employeeList);
    },
    PATCH_DELETE_EMPLOYEE_PROFILE(state, payload) {
      console.log('payload', payload);
      let listIndex = state.employeeList.findIndex(elem => elem.id === payload.id);
      state.employeeList.slice(listIndex, 1);
      console.log('state.employeeList', state.employeeList);
    }

	},
	actions: {
		//Create Methods
    async POSTUser({commit, dispatch, rootState}, payload) {
			return new Promise( async (resolve, reject) => {
				try {
					let endpoint = 'users-profile/';
			
			
					let type = 'Create New User';
					let response = await apiRoutes.POSTItem(dispatch, rootState,payload, endpoint, type);
					console.log('POSTUser response', response);

					commit('PUSH_NEW_USER', response);
					return resolve(response)
					
				} catch (error) {
					console.error("POSTUser error.response", error);
					return reject(response)
				}
			}).catch(error => {
				console.error("POSTUser Promise error.response", error);
        return error;
			});
			
		},
		
		//DELETE Item
		async DELETEUserProfile({commit, dispatch, rootState}, payload) {
			let endpoint = 'users/';
      let type = 'Delete Employee Profile';
			let response = await apiRoutes.DELETEItem(dispatch, rootState,payload, endpoint, type);
			console.log('DELETEProfile response', response);
		},


	},
	getters: {
		GET_USER_LIST(state) {
			return state.userList;
		},
		
	}
}

