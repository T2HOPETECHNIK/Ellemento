import {Entity, model, property, belongsTo} from '@loopback/repository';
import {Location} from './location.model';

@model({settings: {strict: false}})
export class VentilationHistory extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  ventilation_history_id?: number;
  @property({
    type: 'number',
    required: true,
  })
  windspeed: number;

  @property({
    type: 'number',
    required: true,
  })
  temperature: number;

  @property({
    type: 'number',
    required: true,
  })
  humidity: number;

  @property({
    type: 'number',
    required: true,
  })
  co2: number;

  @property({
    type: 'date',
    required: true,
  })
  date_time: string;

  @property({
    type: 'number',
  })
  locationId?: number;

  @belongsTo(() => Location, {name: 'location'})
  location_id: number;
  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<VentilationHistory>) {
    super(data);
  }
}

export interface VentilationHistoryRelations {
  // describe navigational properties here
}

export type VentilationHistoryWithRelations = VentilationHistory & VentilationHistoryRelations;
