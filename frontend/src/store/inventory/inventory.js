import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

import apiRoutes from '@/js/api-routes';

export const Inventory = {
	namespace: true,
	state: {
		inventoryList: [],
		inventoryProfile: {},
		selectedInventoryList: [],
		selectedInventoryProfile: {},
		categoryList: [],
		categoryProfile: {},
		selectedCategoryList: [],
		selectedCategoryProfile: {},
		inventoryGalleryList: [],
		inventoryGalleryProfile: {},
		selectedInventoryGalleryList: [],
		selectedInventoryGalleryProfile: {},

		//POS Module Selected Category
		selectedCategory: '',

	},
	mutations: {
		SET_INVENTORY_LIST(state, payload) {
      // setting price as the sale price or retail price
			var saleItemList = payload.filter(item => item.sale_price != null)
			saleItemList.map(elem => {
				elem['price'] = elem.sale_price;
			});
			var listPriceItemList = payload.filter(item => item.sale_price === null)
			listPriceItemList.map(elem => {
				// console.log("elem", elem);
				elem['price'] = elem.list_price;
			});
			var combined = listPriceItemList.concat(saleItemList);

			state.inventoryList = combined;
    },
    PUSH_NEW_INVENTORY(state, payload) {
      state.inventoryList.push(payload);
		},
		SET_SELECTED_INVENTORY_LIST(state, payload) {
			state.selectedInventoryList = payload
		},
		SET_INVENTORY_PROFILE(state, payload) {
			state.inventoryProfile = payload
		},
		SET_SELECTED_INVENTORY_PROFILE(state, payload) {
			state.selectedInventoryProfile = payload
		},
		UPDATE_INVENTORY_PROFILE_AND_LIST() {
			console.log('payload', payload);
      let listIndex = state.inventoryList.findIndex(elem => elem.id === payload.id);
      state.inventoryList.slice(listIndex, 1);
      state.inventoryList.splice(listIndex, 1, payload);
			console.log('state.inventoryList', state.inventoryList);
			state.inventoryProfile = payload
		},
		UPDATE_SELECTED_INVENTORY_PROFILE_AND_LIST() {
			let listIndex = state.selectedInventoryList.findIndex(elem => elem.id === payload.id);
      state.selectedInventoryList.slice(listIndex, 1);
      state.selectedInventoryList.splice(listIndex, 1, payload);
			console.log('state.selectedInventoryList', state.selectedInventoryList);
			state.selectedInventoryProfile = payload
		},
    PATCH_DELETE_INVENTORY_PROFILE(state, payload) {
      console.log('payload', payload);
      let listIndex = state.inventoryList.findIndex(elem => elem.id === payload.id);
      state.inventoryList.slice(listIndex, 1);
      console.log('state.inventoryList', state.inventoryList);
		},
		//********************************************************************** */

		//Catgories
		PUSH_NEW_INVENTORY_CATEGORY(state, payload) {
			state.categoryList.push(payload);
		},
		SET_CATEGORY_LIST(state, payload) {
			state.categoryList = payload;
		},
		DELETE_INVENTORY_CATEGORY(state, payload) {
			console.log('REMOVE_CATEGORY_LIST payload', payload);
			var indexObj = state.categoryList.findIndex(elem => elem.id === payload);
			console.log('REMOVE_CATEGORY_LIST indexObj', indexObj);
			Vue.delete(state.categoryList, indexObj);
			console.log('REMOVE_CATEGORY_LIST state.categoryList', state.categoryList);
		},

		//Image Gallery
		SET_INVENTORY_IMAGES_LIST(state, payload) {
			state.inventoryGalleryList = payload;
		},
		DELETE_INVENTORY_IMAGE(state, payload) {
			var indexObj = state.inventoryGalleryList.findIndex(elem => elem.id === payload);
			Vue.delete(state.inventoryGalleryList, indexObj);
			console.log('DELETE_INVENTORY_IMAGE state.inventoryGalleryList', state.inventoryGalleryList);
		},

		
	},
	actions: {
		POSTInventory({dispatch}, payload) {
			payload.endpoint = 'inventory/';
			payload.type = 'Create Inventory';
			payload.mutation = 'PUSH_NEW_INVENTORY'
			dispatch("POSTItem",  payload)
		},
		GETInventoryList({dispatch}, payload) {
			payload.endpoint = 'inventory-list/';
			payload.type = 'Get Inventory List';
			payload.mutation = 'SET_INVENTORY_LIST'
			dispatch("GETItemList",  payload)
		},
		GETSelectedInventoryList({dispatch}, payload) {
			payload.endpoint = 'inventory-list/';
			payload.type = 'Get Inventory List';
			payload.mutation = 'SET_SELECTED_INVENTORY_LIST'
			dispatch("GETSelectedItemList",  payload)
		},
		GETInventoryProfile({dispatch}, payload) {
			payload.endpoint = 'inventory/';
			payload.type = 'Get Inventory Profile';
			payload.mutation = 'SET_INVENTORY_PROFILE'
			dispatch("GETItemProfile",  payload)
		},
		GETInventorySelectedProfile({dispatch}, payload) {
			//all selectedMethods need the payload.filterURL from source
			// Using getObjectQueryFilter in the UniversalMixins.js
			payload.endpoint = 'inventory/'+ payload.filterURL;
			payload.type = 'Get Inventory Profile'
			payload.mutation = 'SET_SELECTED_INVENTORY_PROFILE'
			dispatch("GETItemSelectedProfile",  payload)
		},
		PATCHInventoryProfile({dispatch}, payload) {
			payload.endpoint = 'inventory/';
			payload.type = 'Update Inventory';
			payload.mutation = 'UPDATE_INVENTORY_PROFILE_AND_LIST'
			dispatch("PATCHItemProfile",  payload)
		},
		PATCHSelectedInventoryProfile({dispatch}, payload) {
			payload.endpoint = 'inventory/';
			payload.type = 'Update Inventory';
			payload.mutation = 'UPDATE_SELECTED_INVENTORY_PROFILE_AND_LIST'
			dispatch("PATCHSelectedItemProfile",  payload)
		},
		PATCHDeleteProfile({dispatch}, payload) {
			payload.endpoint = 'inventory/';
			payload.type = 'Delete Inventory';
			payload.mutation = 'PATCH_DELETE_INVENTORY_PROFILE'
			dispatch("PATCHDeleteItemProfile",  payload)
		},
		//********************************************************************** */

		//Categories Actions
		POSTCategories({dispatch}, payload) {
			payload.endpoint = 'invcategory/';
			payload.type = 'Create Inventory Category';
			payload.mutation = 'PUSH_NEW_INVENTORY_CATEGORY'
			dispatch("POSTItem",  payload)
		},
		GETInventoryCategories({dispatch}, payload) {
			payload.endpoint = 'invcategory/';
			payload.type = 'Get Inventory Categories';
			payload.mutation = 'SET_CATEGORY_LIST'
			dispatch("GETItemList",  payload)
		},
		DELETEInventoryCategory({dispatch}, payload) {
			payload.endpoint = 'invcategory/';
			payload.type = 'Delete Inventory Category';
			payload.mutation = 'DELETE_INVENTORY_CATEGORY'
			dispatch("DELETEItemProfile",  payload)
		},
		//Inventory Images
		GETInventoryImagesById({dispatch}, payload) {
			payload.endpoint = "inventorygallery/?product="
			payload.type = 'Get Inventory Images';
			payload.mutation = 'SET_INVENTORY_IMAGES_LIST'
			dispatch("GETItemOwnProfile",  payload)
		},
		DELETEInventoryImage({dispatch}, payload) {
			payload.endpoint = "inventorygallery/"
			payload.type = 'Delete Inventory Image';
			payload.mutation = 'DELETE_INVENTORY_IMAGE'
			dispatch("DELETEItemProfile",  payload)
		},

		//POST Inventory
    async POSTItem({commit, dispatch, rootState},  payload) {
      return new Promise( async (resolve, reject) => {
        try {
          let response = await apiRoutes.POSTItem(dispatch, rootState, payload, payload.endpoint, payload.type);
          console.log('POSTInventory response', response);
          commit(payload.mutation, response.data);
          return resolve(response)

        } catch (error) {
          console.error("POSTInventory error.response", error);
					return reject(response)
        }
      }).catch(error => {
        console.error("POSTInventory Promise error.response", error);
        return error;
			});
    },
    //GET Inventory list - Abbreviated List relating to logged in user
    async GETItemList({commit, dispatch, rootState},  payload) {
			let response = await apiRoutes.GETList(dispatch, rootState, payload, payload.endpoint, payload.type);
			console.log('GETItemList response', response);
			commit(payload.mutation, response.data);
		},
		//GET Selected Inventory LIST - Get Abbreviated inventory List of selected company by Parent Company Only
		async GETSelectedItemList({commit, dispatch, rootState}, payload) {
			//filterURL is passed from the original call
			let response = await apiRoutes.GETSelectedList(dispatch, rootState, payload, payload.endpoint, payload.type);
			console.log('GETSelectedItemList response', response);
			commit(payload.mutation, response.data);
		},
     //GET Inventory Profile - Get full details of selected Inventory Item relating to logged in users account
		 GETItemProfile({commit, dispatch, rootState}, payload) {
			return new Promise( async (resolve, reject) => {
				console.log('GETInventoryOwnProfile payload', payload);
				let response = await apiRoutes.GETOwnProfile(dispatch, rootState, payload, payload.endpoint, payload.type);
				console.log('GETItemOwnProfile response', response);
				commit(payload.mutation, response.data[0]);
				return resolve(response.data[0]);
			});
		},
    //GET Selected Profile - Get full details of inventory item of selected company by Parent company only
    async GETItemSelectedProfile({commit, dispatch, rootState}, payload) {
      return new Promise( async (resolve, reject) => {
        let response = await apiRoutes.GETSelectedProfile(dispatch, rootState, payload, payload.endpoint, payload.type);
        console.log('GETItemSelectedProfile response', response);
        commit(payload.mutation, response.data[0]);
        return resolve(response.data[0]);
      });
		},
		//PATCH Profile
		//This endpoint only updates items of itmes relating to user account only
    async PATCHItemProfile({commit, dispatch, rootState}, payload) {
			let response = await apiRoutes.PATCHItem(dispatch, rootState, payload, payload.endpoint, payload.type);
			console.log('PATCHItemProfile response', response);
			commit(payload.mutation, response.data);
		},
		//This endpoint only updates items of itmes relating to user account only
    async PATCHSelectedItemProfile({commit, dispatch, rootState}, payload) {
			let response = await apiRoutes.PATCHItem(dispatch, rootState, payload, payload.endpoint, payload.type);
			console.log('PATCHSelectedItemProfile response', response);
			commit(payload.mutation, response.data);
		},

		//PATCHDelete PROFILE - Changes is_active to false
		//This endpoint only updates items of itmes relating to user account only
    async PATCHDeleteItemProfile({commit, dispatch, rootState}, payload) {
			let response = await apiRoutes.PATCHDeleteItem(dispatch, rootState, payload, payload.endpoint, payload.type);
			console.log('PATCHDeleteItemProfile response', response);
			commit(payload.mutation, payload);
		},
		//DELETEProfile - Actually deleted the item from the db
		async DELETEItemProfile({commit, dispatch, rootState}, payload) {
			let response = await apiRoutes.PATCHDeleteItem(dispatch, rootState, payload, payload.endpoint, payload.type);
			console.log('DELETEItemProfile response', response);
			commit(payload.mutation, payload);
		},
		//Not possible to delete items from sub-accounts from parent
		

	},
	getters: {
		GET_INVENTORY_LIST(state) {
      return state.inventoryList;
		},
		GET_INVENTORY_LIST_LENGTH(state) {
			return state.inventoryList.length;
		},
    GET_OWN_INVENTORY_PROFILE(state) {
      return state.inventoryProfile;
    },
    GET_SELECTED_INVENTORY_PROFILE(state) {
      return state.selectedInventoryProfile;
    },
    GET_INVENTORY_PROFILE(state)   {
      return state.inventoryProfile;
		},
		GET_SELECTED_INVENTORY_LIST(state) {
			return state.selectedInventoryList;
		},
		GET_SELECTED_INVENTORY_LIST_LENGTH(state) {
			return state.selectedInventoryList.length;
		},
		GET_INVENTORY_IMAGE_GALLERY_LIST(state) {
			return state.inventoryGalleryList;
		},
		GET_INV_CATEGORY_LIST(state) {
			return state.categoryList;
		},
		GET_INV_CATEGORY_LIST_LENGTH(state) {
			return state.categoryList.length;
		}
	}
}
