<f7-link icon-ios="f7:lock_open" icon-aurora="f7:lock_open" icon-md="material:lock_open"></f7-link>
<f7-icon material="menu"></f7-icon> Material Design
<f7-icon f7="menu">airplane</f7-icon> F7
<f7-icon icon="icon-back" color="white"></f7-icon> Custom
<f7-icon fa-icon="fa-cc-visa" icon-color="white"></f7-icon> Custom
<f7-icon size="40" icon="mdi mdi-calendar" slot="media"></f7-icon>
<b-icon icon="home" size="is-large"></b-icon> Buefy Icons Material Design
<b-button
  outlined
  type="is-danger"
  icon-pack="mdi" // "fas" also works
  icon-left="arrow-right-circle"
  :disabled="previous.disabled"
  @click.prevent="previous.action">
Previous
</b-button>

<div>
  <f7-button fill class="trans-btn-left" icon="mdi mdi-menu"><span>New Transaction</span></f7-button>
</div>
*************<f7-link icon-size="10" icon="mdi mdi-currency-usd"></f7-link> ***************
Link with Badge
<f7-link icon-only>
  <f7-icon size="50" icon="mdi mdi-account-lock">
    <f7-badge color="red">5</f7-badge>
  </f7-icon>
</f7-link>
dispatch actions            commit mutations
getData(state, getters) {this.$store.getters.<gettername>}

Add a "showINactive" button to show / hide inactive items in database. The user can then reactivate if they desire.

---

Notes:
Usage of BASE_URL
url("#{\$baseURL}assets/images/backgrounds/bg-1.png")

<f7-block v-show="companyForm.id">
</f7-block>

<div for person in people>
<h1> {{ people.firstmname | capitalize }} <h2>

// V-Model
<f7-input type="text"
:value="classdata.title"
@input="classdata.title = \$event.target.value"
placeholder=" ">
</f7-input>

//Checkboxes V-Model
<template>
<input
type="checkbox"
v-for="item in items"
:value="item.id"
:checked="selectedItems.indexOf(item.id) >= 0"
@change="updateSelectedItems"

> </template>

<script>
  ...
  methods: {
    updateSelectedItems(e) {
      const checked = e.target.checked;
      const value = e.target.value;
      if (checked) {
        this.selectedItems.push(value)
      } else {
        this.selectedItems.splice(this.selectedItems.indexOf(value), 1);
      }
    }
  }
</script>

//SmartSelect in Popup

<div class="view view-init">
  <f7-list-item title="Attendees" smart-select :smart-select-params="{openIn: 'popover'}">
    <select name="attendees" multiple>
      <option value="Ian" selected>Ian</option>
      <option value="Joe">Joe</option>
      <option value="Mike">Mike</option>
    </select>
    <b-icon slot="media" icon="account" size="is-medium"></b-icon>
  </f7-list-item>
</div>

//Rendering a list in a select and using V-Model
<f7-input label="Choose Pair:" type="select"
:value="names"
@input="names = \$event.target.value">

  <option v-for="pair in getMyList" :key="pair.id" 
    :value="pair">{{pair}}</option>
</f7-input>

//V-Model
<f7-input
type="text"
:value="classdata.title"
@input="classdata.title = \$event.target.value"
placeholder=" ">
</f7-input>

//Dropdown bindings
<f7-input type="select"
:value="symbolDropdown"
@input="symbolDropdown = $event.target.value">
<option 
      v-for="pair in getMyList" 
      :key="pair.id" 
      :value="pair.name"
      >{{ pair }}</option>
</f7-input>

//Calendar Values. values are an array
<f7-list-input
id="expires"
type="datepicker"
placeholder="Select date"
closeOnSelect="true"
@calendar:change="(values) => invForm.sale_expires.push(...values)"
:calendar-params="{dateFormat: 'DD, MM dd, yyyy'}"
style="background: rgb(216,252,253)">
</f7-list-input>
response: sale_expires: 0: Date Wed Feb 26 2020 00:00:00 GMT-0700 (Mountain Standard Time)

//Toggle Checked pass true false for checked
<f7-toggle @change="userForm.is_something = \$event.target.checked"></f7-toggle>

//Toggle Checked pass custom value
<f7-toggle :value="userIsAdmin" @change="userForm.is_something = \$event.target.value"></f7-toggle>

//Show hide element
v-if="!DataFeed.showCharts ? 'hidden' : ''"
//Show hide parameters
:fill="DataFeed.feedType == 'live'"

//Upating variables on click and passing info
<f7-button name="live" :fill="DataFeed.feedType == 'live'" @click="DataFeed.feedType= \$event.target.name">Live</f7-button>

//Class Binding

<div class="left" v-if="uploadMessage" :class="`message ${error ? 'is-danger': 'is-success'}`">

Default Values for Input Fields
**\* Required. Set value (merchantParent.company_name) in the Mounted() method ** DO NOT use defaultValue
<f7-list-input
v-if="Auth.authLevel === 1"
:disabled="merchantParent.is_datacom === false"
@input="merchantParent.company_name = $event.target.value"
type="select"
class="datacom-input"
:value="Auth.domain === 'datacom' ? merchantParent.company_name : ''">
<option v-for="dataco in Datacom.datacomList" 
    :key="dataco.id">{{ dataco.dba_name }}</option>
</f7-list-input>
<f7-list-item v-if="Auth.authLevel === 2" :title="Auth.userCompanyParent">
<f7-icon slot="media" size="40" icon="mdi mdi-office-building"></f7-icon>
</f7-list-item>

****** Slots ******
--Parent--
<template v-slot:button>
  <f7-row class="display-flex justify-content-center">
    <f7-col width="50">
      Start Below
    </f7-col>
  </f7-row>
</template>
--Child--
<slot name="button"></slot>

**********Passing Data from Child to Parent Component*******
Parent Listen for event
<component @receiveOpenTimes="changeOpenData"></component>
methods(){
changeOpenData(payload) {
this.timeOpenListFromChild = payload;
},
}
Child Emit Event

<div @change="sendToParent" id="idClose">
methods() {
  sendToParent() {
    this.$emit("receiveOpenTimes", this.timeOpenList);
  },
}

***** Get Dates from f7 Datefiled *****
this.holidayForm.date = this.$refs.holidayDatePicker.$refs.inputEl.value;
console.log('this.holidayForm', this.holidayForm);
var year = new Date().getFullYear();
console.log('year', year);
var newDate = new Date(this.holidayForm.date + " " + year);
console.log('newDate', newDate);
console.log('newDate', newDate.toISOString());

<F7 PRELOADERS And DIALOG BOXES>

this.$f7.dialog.progress("Notice: You must enter a valid date");
  setTimeout(() => {
    this.$f7.dialog.close();
  }, 3000);

  this.$f7.dialog.create({
    title: "The title",
    text: "You must enter a valid date",
    buttons: [
      {
        text: "OK",
        bold: true,
        close: true,
        color: "red"
      },
    ],
    closeByBackdropClick: true,
  }).open();

  this.$f7.dialog.alert("Notice: You must enter a valid date");
  this.$f7.dialog.confirm("Notice: You must enter a valid date");
  this.$f7.dialog.prompt("Notice: You must enter a valid date");
  this.$f7.dialog.password("Notice: You must enter a valid date");
  this.$f7.dialog.login("Notice: You must enter a valid date");
  this.$f7.dialog.preloader("Notice: You must enter a valid date");
  this.$f7.dialog.progress("Notice: You must enter a valid date");



selectedPermissions.indexOf(item.id) >= 0

Javascript TEMPLATES with Null Undefined, etc... REMOVE NULL AND UNDEFINED FIRST BY filter(),THEN PERFORM FUNCTION ON RESULT
Empty Object with nested entries --> e.g. --> category.name
category: {}
Object.keys(this.category).length
Object.entries(this.category).length --> Same as above
category: null
Object.entries(this.category)[0][1] != null --> category.id === null

Template Syntax empye Object with nested elements
{{ props.row.category === null ? '' : props.row.category.name }}

Javascript TEMPLASCRIPTES with Null Undefined, etc...
if(this.invCategory.name) {}

****delete icon****
<div><a class="delete"></a></div>
//Use the icon to splice array
<a @click.prevent="files.splice(index, 1)" class="delete"></a>



//Primary ClearForm Option //Option 1
clearFormData() {
console.log("clearFormData this.invForm", this.invForm)
for (let key in this.invForm) {
console.log('key', this.invForm[key]);
if(this.invForm[key] === true || this.invForm[key] === false) {
// console.log('TF key', key);
this.invForm[key] = false;
} else {
this.invForm[key] = null;
}
}
}

//Simple Promise Function
const exists = x => x != null;
const ifExists = value => exists(value) ?
Promise.resolve(value) :
Promise.reject(`Invalid value: ${ value }`);
let answer = ifExists("Hello"); // Invalid value: null
console.log("answer",answer);

//Secondary ClearForm Option
clearForm() {
//Option 2
var $$ = this.Dom7
  var element = $$('input');
for (let key = 0; key<element.length; key++) {
element[key]['value'] = null;
}
console.log("element", element);
},

//Passing several variables to vue method
:checked="selectedPermissions.indexOf(item.id) >= 0"
@change="updateSelectedItems(\$event, props.row.name)"

//Getting values from different state module
addGroupPermissions({ commit, dispatch, context }, permissions) {
var PermisisonList = context.rootState.Permissions.permissionList;
}

//Proper Javascript forloop
for(let item in newGroupObj) {
console.log('newGroupObj[item]', newGroupObj[item]);
}

//Computed Setter
See the userprofile computed section

//Grab Data with Dom7 id="salesNotes"
var $$ = this.Dom7;
var htmlContent = $$("#salesNotes").html();
console.log("htmlContent", htmlContent);

// FindINdex
setIndex({commit, state}) {
const findIndexItem = symbolPrice.findIndex(function(item, index){
return item.symbol == chartsymbol;
});

    OR

var eeIndex = this.Users.employeeList.findIndex(elem => elem.id === rowID);
//My first reduce function this.order.subtotal = this.allItemsInTill.reduce((acc, obj) => {
return acc + parseFloat(obj.list_price);
}, 0);

//Hidden Div tags

<div v-if="!DataFeed.showCharts ? 'hidden' : ''">Please load a chart from the side menu</div>

************\*\*************PYTHON**********\***********

Avoid Circular Reference in Kodels
industry = models.ForeignKey('commons.Industry', on_delete=models.DO_NOTHING, blank=True, null=True)

//Django Multiple Create
mixins.py
class CreateListMixin:
"""Allows bulk creation of a resource."""
def get_serializer(self, *args, \*\*kwargs):
if isinstance(kwargs.get('data', {}), list):
kwargs['many'] = True
return super().get_serializer(*args, \*\*kwargs)

views.py
class HistorViewSet(CreateListMixin, viewsets.ModelViewSet):
queryset = SymbolHistory.objects.all()
serializer_class = HistorySerializer

//Using Moment to converto to UNix
let date = moment("10/15/2014 9:00", "MM/DD/YYYY HH:mm").valueOf()
convert from unix to regualar
let date = moment(1413388800000)format("dddd, MMMM Do YYYY, h:mm:ss a");

//Determine if object is empty
if(Object.keys(this.DataFeed.djangoSymbolHistory).length === 0) {
return this.chart
} else {

//Determine if Array is empty
if(this.DataFeed.djangoSymbolHistory.ohlcv.length == 0) {
return this.chart
} else {

//Python for loop range. Start at end and step backward by -1
for i in range(len(somelist) - 1, -1, -1):
if some_condition(somelist, i):
del somelist[i]

//Reference Store Data from another module
import...
import store from './store';
then use...
var history = store.state.DataFeed.djangoSymbolHistory;

//Using Moment to converto to UNIX
let date = moment("10/15/2014 9:00", "MM/DD/YYYY HH:mm").valueOf()
convert from unix to regualar
let date = moment(1413388800000)format("dddd, MMMM Do YYYY, h:mm:ss a");

//Axios Error Handling
async sendFile() {
const formData = new FormData();
formData.append('file', this.file);
try {
await axios.post('/node/upload/', formData);
this.uploadMessage = "File has been uploaded";
this.file = "";
} catch(err) {
this.uploadMessage = `There was an error uploading ${err.response.data.error}`;
console.log("Error Uploading", err);
this.error = true;
}

//Django managing Files

> > > from django.core.files import File

# Create a Python file object using open()

> > > f = open('/path/to/hello.world', 'w')
> > > myfile = File(f)

//File Storage
from django.core.files.storage import FileSystemStorage
from django.db import models

fs = FileSystemStorage(location='/media/photos')

class Car(models.Model):
...
photo = models.ImageField(storage=fs)

****\*\*****Error Codes******\*\*******
Createcompany
404 bad data
error.response.data.detail - gives no response

Vuex State Rules
I Cannot return a promise from a Mutation
I Can Access rootState in a Mutation if I pass it from the Actions
I cannot access rootState from Mutation d
I cannot return a promise from an Action.

merging Objects in Javascript
Use spread operator
let merged = {...obj1, ...obj2};

TIME
var date_time = moment().format();
console.log('date_time', date_time);
var date_only = moment(date_time).format(moment.HTML5_FMT.DATE);
console.log('date_only', date_only);