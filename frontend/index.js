/* Entry point for Expo
 * This file registers the root component of the app so that it can run in Expo. It imports
 * the App component defined in App.js and registers it as the root component.
 */

import { registerRootComponent } from 'expo';
import App from './App';

// Register the main component so Expo can run it
registerRootComponent(App);
